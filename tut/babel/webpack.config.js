const path = require('path');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    mode: 'development',
    entry: './src/test.webpack.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },

    module:{
        //loaders:[  ]


        rules:[
            {
                test: /\.css$/i,
                use: [
                    'style-loader', 
                    //MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: {
                            importLoaders: 1,
                            module: true,
                        }
                    }
                ],
                include: /\.module\.css$/,
            },

            {
                test: /\.css$/i,
                use: [
                    'style-loader', 
                    'css-loader'
                ],
                exclude: /\.module\.css$/
            },

            {
                test: /\.m?js$/,
                //exclude: /node_modules/,
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

    //plugins: [
    //    new MiniCssExtractPlugin(),
    //],
};
