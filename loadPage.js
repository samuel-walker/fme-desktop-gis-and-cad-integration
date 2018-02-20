//Defines a function to load a Markdown file from GitHub and change its image urls
//Not edited yet
function loadPage(path)
{
  var xhr=createXHR();
  xhr.open("GET", path, true);
  xhr.onreadystatechange=function()
  {
    if(xhr.readyState == 4)
    {
      document.getElementById("zone").innerHTML= xhr.responseText;
    }
  };
  xhr.send(null);
}
