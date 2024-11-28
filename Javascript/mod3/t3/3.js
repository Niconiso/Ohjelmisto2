'use strict';

const target = document.getElementById('target');

const names = ['John', 'Paul', 'Jones'];
let htmlContent = '';
for (let i = 0; i < names.length; i++) {
    htmlContent += `<li>${names[i]}</li>`;
}
target.innerHTML = htmlContent;