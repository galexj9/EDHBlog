function randomColor() {
    var color = '#' + Math.floor(Math.random()*16777215).toString(16);
    document.getElementById("color-button").style.backgroundColor = color;
  }