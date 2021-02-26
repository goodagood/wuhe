
import json from '@rollup/plugin-json';

export default {
    input: './main.js',
    output: {
        file: 'bundle.js',
        format: 'cjs'
    },
    plugins: [json(), ]
};
