import  React, { Component } from  'react';
import ArticleService from './ArticlesService';

const  articlesService  =  new  ArticleService();


class  ArticlesList  extends  Component {

	constructor(props) {
		super(props);
		this.state  = {
			articles: [],
			nextPageURL:  ''
		};
		this.nextPage  =  this.nextPage.bind(this);
		this.handleDelete  =  this.handleDelete.bind(this);
	}


    componentDidMount() {
        var  self  =  this;
        articlesService.getArticles().then(function (result) {
            self.setState({ articles:  result.data, nextPageURL:  result.nextlink})
        });
    }


    handleDelete(e,pk){
        var  self  =  this;
        articlesService.deleteArticle({pk :  pk}).then(()=>{
            var  newArr  =  self.state.customers.filter(function(obj) {
                return  obj.pk  !==  pk;
            });
            self.setState({articles:  newArr})
        });
    }

    nextPage(){
	var  self  =  this;
	articlesService.getArticlesByURL(this.state.nextPageURL).then((result) => {
		self.setState({ articles:  result.data, nextPageURL:  result.nextlink})
	});
    }

    render() {
        // {this.state.articles.map( c =>
        //     console.log(c.title)
        // )}
        let a = {"aa": "aa"}
        console.log(a.aa)
        console.log(this.state.articles)

        return(
            <div>
                {this.state.articles.map( c =>
            c.title
        )}
                ERWSGRDDFHDFGH
            </div>
        )
    }
}
export  default  ArticlesList;