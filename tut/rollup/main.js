
import foo from './foo.js';

import { version } from './package.json';

function showVersion(){
    console.log('version: ' + version);
}


//export { showVersion, }

export default function () {
  console.log(foo);
}

