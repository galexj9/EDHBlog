function randomColorBackground(element) {
    var color = '#' + Math.floor(Math.random()*16777215).toString(16);
    document.getElementById(element).style.backgroundColor = color;
  }

  function randomColorBorder(element) {
    var color = '#' + Math.floor(Math.random()*16777215).toString(16);
    document.getElementById(element).style.borderColor = color;
  }