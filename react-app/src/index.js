import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

// class Square extends React.Component {
//   render() {
//     return (
//       <button className="square"
//               onClick={() => this.props.onClick()}
//       >
//         {this.props.value}
//       </button>
//     );
//   }
// }

function Square(props) {
    return(
        <button className="square" onClick={props.onClick}>
            {props.value}
        </button>
    );
}

class Board extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
          squires: Array(9).fill(null),
          xIsNext: true,
      }
  }

  handleClick(i) {
      const squires = this.state.squires.slice();
      squires[i] = this.state.xIsNext ? 'X' : 'O';
      this.setState({
          squires: squires,
          xIsNext: !this.state.xIsNext,
      });
  }

  renderSquare(i) {
    return (<Square
        value={this.state.squires[i]}
        onClick={() => this.handleClick(i)}
    />);
  }

  render() {
    const status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');

    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);
