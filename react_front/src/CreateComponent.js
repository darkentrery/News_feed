import React, {Component, useState, useEffect, useRef} from "react";
import ArticleService from './ArticlesService';
import {Link} from "react-router-dom";

const  articlesService  =  new  ArticleService();




export default function CreateComponent () {
    const [title, setTitle] = useState(false)
    const [anons, setAnons] = useState(false)
    const [full_text, setText] = useState(false)
    const [date_public, setDate_public] = useState(new Date())
    const [photo, setPhoto] = useState(false)
    const [date, setDate] = useState(new Date())

    const [data, setData] = useState("No");


    useEffect(() => {
        let bodyFormData = new FormData();
        bodyFormData.append('title', title);
        bodyFormData.append('anons', anons);
        bodyFormData.append('full_text', full_text);
        bodyFormData.append('photo', photo);
        bodyFormData.append('date', new Date(date).toLocaleDateString());
        setData(bodyFormData)
    }, [title, anons, full_text, date, photo])

    const sendForm = () => {
        if (title && anons && full_text && date && photo) {
            console.log(data)
            console.log(data.photo)
            articlesService.createArticle(data)
            console.log(data.photo)
        }

    }

    return(
        <div>
            <form >
                <label>Title</label><br/>
                <input className="form-control" type="text"  onChange={(event) => setTitle(event.target.value)}/><br/><br/>
                <label>Anons</label><br/>
                <input className="form-control" type="text"  onChange={(event) => setAnons(event.target.value)}/><br/><br/>
                <label>Text</label><br/>
                <textarea className="form-control"  onChange={(event) => setText(event.target.value)}/><br/><br/>
                <label>Date public</label><br/>
                <input className="form-control" type="date" value={date} onChange={(event) => setDate(event.target.value)}/><br/><br/>
                <label>Photo</label><br/>
                <input className="form-control" type="file" name="myImage" accept="image/*" onChange={(event) => setPhoto(event.target.files[0])}/><br/><br/>
                {photo && (
                    <div>
                        <img alt="not fount" width={"250px"} src={URL.createObjectURL(photo)} />
                        <br />
                        <button onClick={()=>setPhoto(null)}>Remove</button>
                    </div>
                )}

                <button onClick={sendForm}>Send</button>
            </form><br/><br/>
        </div>
    )
}