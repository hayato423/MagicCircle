const radius = 245;
const circleThickness = 10;
var thicknessSlider;
var penOrEraserRadio;
var canvas;

const xhr = new XMLHttpRequest();

function setup() {
    let canvas = createCanvas(500,500);
    canvas.parent('canvas');
    frameRate(60);
    background(0);
    //全消去ボタン
    const clearButton = createButton("clear");
    clearButton.mousePressed(clearCanvas);
    // clearButton.position(0, 40);
    clearButton.parent('reset');
    clearButton.id('clear-button')
    //太さスライダー
    thicknessSlider = createSlider(0, 10, 5);
    // thicknessSlider.position(50, 15);
    thicknessSlider.parent('slider');
    thicknessSlider.id('thick-slider')
    //ラジオボタン
    penOrEraserRadio = createRadio();
    penOrEraserRadio.option('pen');
    penOrEraserRadio.option('eraser');
    penOrEraserRadio.style('width', '200px');
    penOrEraserRadio.id('radio-button')
    // penOrEraserRadio.position(340, 10);
    penOrEraserRadio.selected('pen');
    penOrEraserRadio.parent('option');
    //保存ボタン
    const uploadButton = createButton('Activate');
    uploadButton.mousePressed(upload);
    uploadButton.parent('upload');
    uploadButton.id('upload-button')

    //初期化描画
    initDraw();
}

function draw() {
    if (mouseIsPressed) {
        const centerX = width / 2, centerY = height / 2;
        const mouseDistance = Math.pow(mouseX - centerX, 2) + Math.pow(mouseY - centerY, 2);
        const pmouseDistance = Math.pow(pmouseX - centerX, 2) + Math.pow(pmouseY - centerY, 2);
        const radiusDistance = pow(radius - circleThickness + 2, 2);
        //マウスカーソルが円の中なら線を描画
        if (mouseDistance <= radiusDistance && pmouseDistance <= radiusDistance) {
            strokeWeight(thicknessSlider.value());
            if (penOrEraserRadio.value() == 'pen') {
                stroke(255);
            } else {
                stroke(0);
            }
            line(pmouseX, pmouseY, mouseX, mouseY);
        }
    }
}

function clearCanvas() {
    background(0);
    initDraw();
}

function initDraw() {
    // fill(0);
    // textSize(16);
    // strokeWeight(0);
    // text('太さ', 0, 20);
    strokeWeight(circleThickness);
    noFill();
    stroke(255);
    ellipse(width / 2, height / 2, radius * 2, radius * 2);
}

function upload() {
    const canvas = document.getElementById("defaultCanvas0");
    const image = canvas.toDataURL('image/png');
    const url = "http://192.168.0.123:8000/magic_circle/upload/";
    let csrftoken = '';
    const formData = new FormData();
    const cookies = document.cookie;
    const cookiesArray = cookies.split(';');
    for(var c of cookiesArray) {
        var cArray = c.split('=');
        if(cArray[0] == 'csrftoken'){
            csrftoken = cArray[1];
        }
    }

    formData.append('picture',image);
    xhr.open("POST",url);
    xhr.setRequestHeader('enctype',"multipart/form-data");
    xhr.setRequestHeader('X-CSRFToken',csrftoken);
    xhr.send(formData);
}


function save() {
    const canvas = document.getElementById("defaultCanvas0");
    const image = canvas.toDataURL('image/jpg');
    const a = document.createElement('a');
    a.href = image;
    a.download = 'canvas.png';
    a.click();
}

window.onload = function no_scroll() {
    document.addEventListener("touchmove",scrroll_control,{passive:false});
}

function scrroll_control(event){
    event.preventDefault();
}