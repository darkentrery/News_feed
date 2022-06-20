import React, {Component, useState, useEffect} from "react";
import ArticleService from './ArticlesService';
import {Link, useLocation} from "react-router-dom";
import {Pagination, PaginationItem} from "@mui/material";
const  articlesService  =  new  ArticleService();



export default function HomeComponent ({updatePk}) {
    let location = useLocation()
    const [data, setData] = useState(0);
    const [pages, setPages] = useState([]);
    const [page, setPage] = useState(location.search?.split('=')[1] || 1);
    console.log(location)
    console.log("Page = ", page)
    console.log(updatePk)


    useEffect(() => {
        articlesService.getArticlesByURL(`/api/articles/?page=${page}`).then((result) =>
        {setData(result.results)
            console.log(result)}
        );
        articlesService.getArticlesByURL(`/api/articles/?page=1`).then((result) =>
        {if (result.count) {
            setPages(Math.ceil(result.count / result.results.length))
        } else {
            setPages(0)
        }}
        );
        console.log(pages)
        console.log("!!!")
    }, [page]);


    if (data) {

        console.log(data)
        console.log(pages)


        return(

        <div>
            {data.map(d =>
                <div className="alert alert-warning">
                    <h3 key="{d.title}">{d.title}</h3>
                    <p key="{d.anons}">{d.anons}</p>
                    <p key="{d.date}">{new Date(d.date).toLocaleDateString()}</p>
                    <p key="{photo}">photo</p>
                    <p><img src={d.photo} alt=""/></p>
                    <p>
                        <nav>
                            <Link to={`/?pk=${d.pk}`}>
                                <button className="btn btn-warning" onClick={() =>
                                updatePk(d.pk)}>Read detail</button>
                            </Link>
                        </nav>
                    </p>
                </div>
            )}
            {pages &&
                <div className="alert alert-warning">
                <Pagination count={pages}
                            color="primary"
                            onChange={(event, page) => setPage(page)}
                            renderItem={
                                (item) => (
                                    <PaginationItem
                                        component={Link}
                                        to={`/home/?page=${item.page}`}
                                        {...item}

                                    />
                                )
                                }/>
            </div>

            }





        </div>
        )
    }
}