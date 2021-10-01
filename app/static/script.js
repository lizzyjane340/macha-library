// script for darkmode.js widget begin
    function addDarkmodeWidget() {
          new Darkmode().showWidget();
        }

    window.addEventListener('load', addDarkmodeWidget); 
  
    const options = {
    bottom: '32px', 
    right: '32px', 
    left: 'unset', 
    time: '0.7s', 
    mixColor: '#fff', 
    backgroundColor: '#fff', 
    buttonColorDark: '#000',  
    buttonColorLight: '#FFF', 
    saveInCookies: true, 
    label: '🌓', 
    autoMatchOsTheme: false
    } 
 
    const darkmode = new Darkmode(options);
        
    darkmode.showWidget();

// date widget for navbar 
var months = ['January','February','March','April','May','June','July',
'August','September','October','November','December'];

var date = new Date();

document.getElementById('spanDate').innerHTML = "session: " + date.toUTCString();

// file upload alert
let uploadFile = document.getElementById('entry-file');

if (uploadFile != null) {
  uploadFile.addEventListener('change', () => {
    document.getElementById('uploadLabel').innerHTML = "File Uploaded";
  });
}

// input length validation for forms
const loginUsername = document.getElementById('loginUsername');

if (loginUsername != null) {  
  loginUsername.addEventListener('input', () => {
  if (loginUsername.validity.invalid) {
    loginUsername.setCustomValidity = "Username should be 3 to 15 characters";
  } else {
    loginUsername.setCustomValidity("");
  }
  });
}

const loginPassword = document.getElementById('loginPassword');

if (loginPassword != null) {
  loginPassword.addEventListener('input', () => {
    if (!loginPassword.checkValidity()) {
      loginPassword.innerHTML = loginPassword.validationMessage;
    } 
  });
}

const usernameReg = document.getElementById('usernameReg');

if (usernameReg != null) {
  usernameReg.addEventListener('input', () => {
    if (usernameReg.checkValidity()) {
      usernameReg.innerHTML = usernameReg.validationMessage;
    } 
  });
}

const uniqueCode = document.getElementById('uniqueCodeBlock');

if (uniqueCode != null) {
  uniqueCode.addEventListener('input', () => {
    if (uniqueCode.checkValidity()) {
      uniqueCode.innerHTML = uniqueCode.validationMessage;
    } 
  });
}

const passwordReg1 = document.getElementById('passwordReg1');
const passwordReg2 = document.getElementById('passwordReg2');

if (passwordReg1 != null) {
  passwordReg1.addEventListener('input', () => {
      if (passwordReg1.checkValidity()) {
          passwordReg1.innerHTML = passwordReg1.validationMessage;
      } 
  });
}

if (passwordReg2 != null){
  passwordReg2.addEventListener('input', () => {
    if (passwordReg2.checkValidity()) {
        passwordReg2.innerHTML = passwordReg2.validationMessage;
    } 
});
}

const entryTitle = document.getElementById('entryTitle');
const entryLink = document.getElementById('entryLink');
const entryDesc = document.getElementById('entryDesc');

if (entryTitle, entryLink, entryDesc != null) {

entryTitle.addEventListener('input', () => {
    if (entryTitle.checkValidity()) {
        entryTitle.innerHTML = entryTitle.validationMessage;
    } 
});

entryLink.addEventListener('input', () => {
    if (entryLink.checkValidity()) {
        entryLink.innerHTML = entryLink.validationMessage;
    } 
});

entryDesc.addEventListener('input', () => {
    if (entryDesc.checkValidity()) {
        entryDesc.innerHTML = entryDesc.validationMessage;
    } 
});
}

//const catCheck = document.getElementById('catCheck');
// TODO checkbox validation entry form
//catCheck.addEventListener('change')



