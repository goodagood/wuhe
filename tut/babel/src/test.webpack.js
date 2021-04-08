import _ from 'lodash';

import './style.css';
import styles from './app.css';

import greetings from './robot.js';

//?
import './babel.es6.al.js';

document.write(greetings("Affirmative", "Dave"));
document.write("<p> add a p </p>");

// test to require another local js file
//require( './alert.msg.js');

function component() {
    const element = document.createElement('div');

    element.innerHTML = _.join(['Hello', 'webpack', ', hoho，', Date().toString() ], ' ');
    element.classList.add('.test_webpack');

    document.wpele = element;
    return element;
}

document.body.appendChild(component());



var element = `
  <div class="element">
  <p>
Loaders are transformations that are applied to the source code of a module. They allow you to pre-process files as you import or “load” them. Thus, loaders are kind of like “tasks” in other build tools and provide a powerful way to handle front-end build steps. Loaders can transform files from a different language (like TypeScript) to JavaScript or load inline images as data URLs. Loaders even allow you to do things like import CSS files directly from your JavaScript modules!
</p>
  </div>
`

document.write(element);
