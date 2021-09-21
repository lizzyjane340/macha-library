// script for darkmode.js widget begin
    function addDarkmodeWidget() {
          new Darkmode().showWidget();
        }

    window.addEventListener('load', addDarkmodeWidget); 
  
    const options = {
    bottom: '32px', 
    right: '32px', 
    left: 'unset', 
    time: '0.5s', 
    mixColor: '#fff', 
    backgroundColor: '#fff', 
    buttonColorDark: '#000',  
    buttonColorLight: '#FFF', 
    saveInCookies: true, 
    label: '🌓', 
    autoMatchOsTheme: true
    } 
 
    const darkmode = new Darkmode(options);
        
    darkmode.showWidget();

// date widget for navbar 
var months = ['January','February','March','April','May','June','July',
'August','September','October','November','December'];

var date = new Date();

document.getElementById("spanDate").innerHTML = "session: " + date.toUTCString();

// file upload alert
let uploadFile = document.getElementById('entry-file');

uploadFile.addEventListener('change', () => {
    document.getElementById('uploadLabel').innerHTML = "File Uploaded";
});