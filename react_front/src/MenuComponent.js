import React, {Component, useState} from "react";
import logo1 from "./sibers-logo.svg";
import HomeComponent from "./HomeComponent";
import {BrowserRouter as Router, Link, Route, Routes, useLocation} from "react-router-dom";
import {Pagination} from "@mui/material";

// eslint-disable-next-line react-hooks/rules-of-hooks


export default function MenuComponent () {
     let location = useLocation()
    console.log(location)
    console.log("Menu")
    return(
        <div>
            <aside>
                <img className="logo-icon" src={logo1} alt="logo"/>
                <span className="logo">News</span>
                <h3>Navigation</h3>

                <nav>
                     <ul>
                            <li>
                                <Link to={`/home`}><h3>Home</h3></Link>
                            </li>
                            <li>
                                <Link to="/about" ><h3>About</h3></Link>
                            </li>
                            <li>
                                <Link to="/users" ><h3>Users</h3></Link>
                            </li>
                            <li>
                                <Link to="/create" >
                                    <button className="btn btn-info"><i className="fas fa-plus-circle"></i>Add
                                            article
                                    </button>
                                </Link>
                            </li>
                        </ul>
                </nav>

            </aside>

        </div>


    )
}