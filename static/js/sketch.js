const radius = 150;
const circleThickness = 10;
var thicknessSlider;
var penOrEraserRadio;
var canvas;

const xhr = new XMLHttpRequest();

function setup() {
    canvas = createCanvas(400, 400);
    frameRate(60);
    background(255);
    //全消去ボタン
    const clearButton = createButton("リセット");
    clearButton.mousePressed(clearCanvas);
    clearButton.position(0, 40);
    //太さスライダー
    thicknessSlider = createSlider(0, 10, 5);
    thicknessSlider.position(50, 15);
    //ラジオボタン
    penOrEraserRadio = createRadio();
    penOrEraserRadio.option('pen');
    penOrEraserRadio.option('eraser');
    penOrEraserRadio.style('width', '70px');
    penOrEraserRadio.position(340, 10);
    penOrEraserRadio.selected('pen');
    //保存ボタン
    const uploadButton = createButton('Upload');
    uploadButton.mousePressed(upload);

    const saveButton = createButton('save');
    saveButton.mousePressed(save);
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
                stroke(0);
            } else {
                stroke(255);
            }
            line(pmouseX, pmouseY, mouseX, mouseY);
        }
    }
}

function clearCanvas() {
    background(255);
    initDraw();
}

function initDraw() {
    // fill(0);
    // textSize(16);
    // strokeWeight(0);
    // text('太さ', 0, 20);
    strokeWeight(circleThickness);
    noFill();
    stroke(0);
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
    const image = canvas.toDataURL('image/png');
    const a = document.createElement('a');
    a.href = image;
    a.download = 'canvas.png';
    a.click();
}

