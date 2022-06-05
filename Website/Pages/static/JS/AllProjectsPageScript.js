function MyFunction(){
var a = document.getElementById("myLink");
var linkText = document.createTextNode("Human Resurces");
a.appendChild(linkText);
a.title = "Human Resurces";
a.href = "mainHomepage/index.html";
document.body.appendChild(a);
}
