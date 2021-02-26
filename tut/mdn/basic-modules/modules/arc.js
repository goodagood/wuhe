const name = 'circle';

function circle(ctx, x, y,radius,  color) {
    ctx.fillStyle = color; //?

    ctx.beginPath();
    //ctx.arc(x, y, radius, sAngle, eAngle);

    var gradient = ctx.createLinearGradient(0, 0, ctx.lineWidth, 0)
    gradient.addColorStop("0", "red");
    gradient.addColorStop("0.5", "green");
    gradient.addColorStop("1.0", "blue");

    ctx.strokeStyle = gradient;

    ctx.arc(x, y, radius, 0, Math.PI * 2);

    ctx.lineWidth = 5;

    //ctx.stroke();
    ctx.fill();

    return {
        radius: radius,
        x: x,
        y: y,
        color: color
    };
}

function random(min, max) {
   let num = Math.floor(Math.random() * (max - min)) + min;
   return num;
}

function reportArea(length, listId) {
  let listItem = document.createElement('li');
  listItem.textContent = `${name} area is ${length * length}px squared.`

  let list = document.getElementById(listId);
  list.appendChild(listItem);
}

function reportPerimeter(length, listId) {
  let listItem = document.createElement('li');
  listItem.textContent = `${name} perimeter is ${length * 4}px.`

  let list = document.getElementById(listId);
  list.appendChild(listItem);
}

function randomCircle(ctx) {
    let color1 = random(0, 255);
    let color2 = random(0, 255);
    let color3 = random(0, 255);
    let color = `rgb(${color1},${color2},${color3})`
    ctx.fillStyle = color;

    let x = random(0, 480);
    let y = random(0, 320);
    let radius = random(10, 100);
    //ctx.fillRect(x, y, length, length);

    circle(ctx, x, y, radius, color)


    return {
        'radius': radius,
        x: x,
        y: y
    };
}

export { name, circle, reportArea, reportPerimeter };
export default randomCircle;
