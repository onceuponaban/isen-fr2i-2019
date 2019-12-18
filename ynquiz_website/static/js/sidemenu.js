function toggleNav()
{
    currentWidth = document.getElementById("sideMenu").style.width;
    newWidth = currentWidth == "250px" ? "0" : "250px";
    document.getElementById("sideMenu").style.width = newWidth;
}

function closeNav()
{
    document.getElementById("sideMenu").style.width = "0";
} 