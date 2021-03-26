

function hundredMap(percentStr, arrayLen){
    // map hundred percent (without percent symbol) to array length,
    // use Math.random to make sure all the array index get a chance
    var i = parseInt(percentStr);
    if( i < 0){
        return 0;
    }
    
    var scale = arrayLen / 100;
    if(scale > 1){
        var guess = Math.floor( i * scale + scale * Math.random());
        if(guess > arrayLen){ guess = arrayLen };
        return guess
    }

    return Math.floor( i * scale );
}


