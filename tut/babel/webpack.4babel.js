// Can't we name this to 'webpack.babel.js' instead of webpack.4babel.js?
// I got trouble for it.


const path = require('path');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    mode: 'development',
    entry: './src/babel.es6.al.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'babel.es6.al.js',
    },

    module:{

        rules:[


            {
                test: /\.m?js$/,
                include: __dirname + 'src',
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env',]
                    }
                }
            }
        ],
    },

};
