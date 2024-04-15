console.log("JS work!");
let btn = document.querySelector(".ploooow");
let txt = document.querySelector("#txtfottheme");

console.log(txt);
console.log(btn);

// РЕАЛИЗУЕМ ФУНКЦИЮ КОТОРАЯ БУДЕТ ИЗМЕНЯТЬ ТЕМУ
function theme_change() {
  btn.style.color = "white";
}

btn.addEventListener("click", theme_change);
