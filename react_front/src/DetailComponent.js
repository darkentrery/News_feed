import React, {Component, useState, useEffect} from "react";
import ArticleService from './ArticlesService';

const  articlesService  =  new  ArticleService();


export default function DetailComponent ({pk}) {
    const [data, setData] = useState(0);

    console.log("Pk = ", pk)

    useEffect(() => {
        articlesService.getArticle(pk).then((result) =>
            setData(result)
        );
    }, [pk]);

    console.log(data)

    if (data != 0) {
        return(
        <div>
                <div className="alert alert-warning">
                    <h3 key="{data.title}">{data.title}</h3>
                    <p key="{data.anons}">{data.anons}</p>
                    <p key="{data.date}">{new Date(data.date).toLocaleDateString()}</p>
                    <p key="{photo}">photo</p>
                    {data.photo &&
                    <p><img src={"http://127.0.0.1" + data.photo} alt=""/></p>}
                    <p><button onClick={() => articlesService.deleteArticle(data)}>Delete</button></p>

                </div>
        </div>
        )
    }
}