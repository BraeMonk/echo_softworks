# -*- coding: utf-8 -*-
# scripts_data.py
#
# Source of truth for every skeleton script on echosoftwork.com/scripts.html.
# To add a new script: copy an entry below, fill it in, run generate.py,
# then commit the regenerated scripts-data.js (and scripts.html if you
# changed the filter categories).

SCRIPTS = [
    {
        "slug": "servo-sweep",
        "title": "Servo Sweep & Position Control",
        "summary": "Get a servo moving predictably before you touch your real project.",
        "category": "hardware",
        "tags": ["motor & servo", "embedded"],
        "langs": [
            {"id": "cpp", "label": "Arduino C++", "code": """#include <Servo.h>

// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const int SERVO_PIN   = 9;     // TODO: your PWM-capable pin
const int MIN_ANGLE   = 0;
const int MAX_ANGLE   = 180;
const int STEP_DELAY  = 15;    // ms between steps

Servo myServo;
int angle = MIN_ANGLE;
int direction = 1;

void setup() {
  myServo.attach(SERVO_PIN);
  myServo.write(angle);
}

void loop() {
  myServo.write(angle);
  angle += direction;

  if (angle >= MAX_ANGLE || angle <= MIN_ANGLE) {
    direction *= -1;
  }
  delay(STEP_DELAY);

  // TODO: replace the sweep with your real logic
}

void moveTo(int targetAngle) {
  targetAngle = constrain(targetAngle, MIN_ANGLE, MAX_ANGLE);
  myServo.write(targetAngle);
}"""},
            {"id": "python", "label": "CircuitPython", "code": """import time
import board
import pwmio
from adafruit_motor import servo

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
SERVO_PIN = board.D9      # TODO: your PWM-capable pin
MIN_ANGLE = 0
MAX_ANGLE = 180
STEP_DELAY = 0.015

pwm = pwmio.PWMOut(SERVO_PIN, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

angle = MIN_ANGLE
direction = 1

def move_to(target_angle):
    target_angle = max(MIN_ANGLE, min(MAX_ANGLE, target_angle))
    my_servo.angle = target_angle

while True:
    my_servo.angle = angle
    angle += direction

    if angle >= MAX_ANGLE or angle <= MIN_ANGLE:
        direction *= -1

    time.sleep(STEP_DELAY)

    # TODO: replace the sweep with your real logic"""},
        ],
    },
    {
        "slug": "dc-motor-driver",
        "title": "DC Motor \u2014 PWM Driver",
        "summary": "Direction and speed control through a standard H-bridge (L298N / TB6612-style).",
        "category": "hardware",
        "tags": ["motor & servo", "embedded"],
        "langs": [
            {"id": "cpp", "label": "Arduino C++", "code": """// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const int PIN_IN1 = 5;   // TODO: H-bridge input 1
const int PIN_IN2 = 6;   // TODO: H-bridge input 2
const int PIN_PWM = 9;   // TODO: enable / speed pin

void setup() {
  pinMode(PIN_IN1, OUTPUT);
  pinMode(PIN_IN2, OUTPUT);
  pinMode(PIN_PWM, OUTPUT);
  stopMotor();
}

void loop() {
  // TODO: replace this demo pattern with real control logic
  forward(180);   delay(1500);
  stopMotor();    delay(400);
  backward(180);  delay(1500);
  stopMotor();    delay(400);
}

void forward(int speed) {
  digitalWrite(PIN_IN1, HIGH);
  digitalWrite(PIN_IN2, LOW);
  analogWrite(PIN_PWM, constrain(speed, 0, 255));
}

void backward(int speed) {
  digitalWrite(PIN_IN1, LOW);
  digitalWrite(PIN_IN2, HIGH);
  analogWrite(PIN_PWM, constrain(speed, 0, 255));
}

void stopMotor() {
  digitalWrite(PIN_IN1, LOW);
  digitalWrite(PIN_IN2, LOW);
  analogWrite(PIN_PWM, 0);
}"""},
            {"id": "python", "label": "Raspberry Pi (Python)", "code": """import RPi.GPIO as GPIO
import time

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
PIN_IN1 = 17
PIN_IN2 = 27
PIN_PWM = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)
GPIO.setup(PIN_PWM, GPIO.OUT)
pwm = GPIO.PWM(PIN_PWM, 1000)
pwm.start(0)

def forward(speed):
    GPIO.output(PIN_IN1, GPIO.HIGH)
    GPIO.output(PIN_IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(max(0, min(100, speed)))

def backward(speed):
    GPIO.output(PIN_IN1, GPIO.LOW)
    GPIO.output(PIN_IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(max(0, min(100, speed)))

def stop_motor():
    GPIO.output(PIN_IN1, GPIO.LOW)
    GPIO.output(PIN_IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

try:
    # TODO: replace this demo pattern with real control logic
    while True:
        forward(70);  time.sleep(1.5)
        stop_motor(); time.sleep(0.4)
        backward(70); time.sleep(1.5)
        stop_motor(); time.sleep(0.4)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()"""},
        ],
    },
    {
        "slug": "addressable-led",
        "title": "Addressable LED Pattern",
        "summary": "A rotating rainbow across a NeoPixel/WS2812 strip \u2014 swap the pattern math for your own.",
        "category": "hardware",
        "tags": ["lighting", "embedded"],
        "langs": [
            {"id": "cpp", "label": "Arduino C++ (FastLED)", "code": """#include <FastLED.h>

// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
#define LED_PIN     6      // TODO: your data pin
#define NUM_LEDS    30
#define BRIGHTNESS  80

CRGB leds[NUM_LEDS];

void setup() {
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(BRIGHTNESS);
}

void loop() {
  // TODO: replace with your real pattern
  static uint8_t hue = 0;
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CHSV(hue + (i * 256 / NUM_LEDS), 255, 255);
  }
  FastLED.show();
  hue++;
  delay(20);
}"""},
            {"id": "python", "label": "CircuitPython", "code": """import board
import neopixel
import time

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
LED_PIN = board.D6
NUM_LEDS = 30
BRIGHTNESS = 0.3

pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

def wheel(pos):
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

hue = 0
while True:
    # TODO: replace with your real pattern
    for i in range(NUM_LEDS):
        pixel_index = (i * 256 // NUM_LEDS) + hue
        pixels[i] = wheel(pixel_index & 255)
    pixels.show()
    hue = (hue + 1) % 256
    time.sleep(0.02)"""},
        ],
    },
    {
        "slug": "temp-humidity-sensor",
        "title": "Temperature & Humidity Sensor Reader",
        "summary": "Poll a DHT22 on an interval and hand off clean readings, with bad-read retries baked in.",
        "category": "hardware",
        "tags": ["sensors", "embedded"],
        "langs": [
            {"id": "cpp", "label": "Arduino C++", "code": """#include <DHT.h>

// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
#define DHT_PIN     2        // TODO: your data pin
#define DHT_TYPE    DHT22
const unsigned long READ_INTERVAL = 2000;  // ms, DHT22 min ~2s

DHT dht(DHT_PIN, DHT_TYPE);
unsigned long lastRead = 0;

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  if (millis() - lastRead >= READ_INTERVAL) {
    lastRead = millis();
    readSensor();
  }
  // TODO: replace the Serial print with your real logic
}

void readSensor() {
  float humidity = dht.readHumidity();
  float tempC = dht.readTemperature();

  if (isnan(humidity) || isnan(tempC)) {
    Serial.println("Read failed, will retry next interval");
    return;
  }

  Serial.print("Temp: "); Serial.print(tempC);
  Serial.print("C  Humidity: "); Serial.print(humidity); Serial.println("%");
}"""},
            {"id": "python", "label": "CircuitPython", "code": """import time
import board
import adafruit_dht

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
DHT_PIN = board.D2       # TODO: your data pin
READ_INTERVAL = 2.0      # seconds, DHT22 min ~2s

dht = adafruit_dht.DHT22(DHT_PIN)

def read_sensor():
    try:
        temp_c = dht.temperature
        humidity = dht.humidity
        print(f"Temp: {temp_c}C  Humidity: {humidity}%")
        return temp_c, humidity
    except RuntimeError as e:
        # DHT sensors drop reads often \u2014 this is normal, just retry
        print(f"Read failed ({e.args[0]}), will retry next interval")
        return None, None

while True:
    read_sensor()   # TODO: replace with your real logic
    time.sleep(READ_INTERVAL)"""},
        ],
    },
    {
        "slug": "button-debounce",
        "title": "Button Input & Debounce",
        "summary": "Clean single-press detection from a noisy mechanical switch \u2014 no phantom double-fires.",
        "category": "hardware",
        "tags": ["input", "embedded"],
        "langs": [
            {"id": "cpp", "label": "Arduino C++", "code": """// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const int BUTTON_PIN = 2;         // TODO: your input pin
const unsigned long DEBOUNCE_MS = 40;

int lastReading = HIGH;
int stableState = HIGH;
unsigned long lastChangeTime = 0;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_PIN, INPUT_PULLUP);   // wired to GND when pressed
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);

  if (reading != lastReading) {
    lastChangeTime = millis();
  }

  if (millis() - lastChangeTime > DEBOUNCE_MS) {
    if (reading != stableState) {
      stableState = reading;
      if (stableState == LOW) {
        onPress();   // TODO: replace with your real logic
      }
    }
  }

  lastReading = reading;
}

void onPress() {
  Serial.println("Button pressed");
}"""},
            {"id": "python", "label": "Raspberry Pi (Python)", "code": """import RPi.GPIO as GPIO
import time

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
BUTTON_PIN = 17     # TODO: your input pin
DEBOUNCE_MS = 200

def on_press(channel):
    # TODO: replace with your real logic
    print("Button pressed")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
                       callback=on_press, bouncetime=DEBOUNCE_MS)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()"""},
        ],
    },
    {
        "slug": "web-app-starter",
        "title": "Web App Starter, No Build Step",
        "summary": "State, render, and event handling in one file \u2014 open it and go.",
        "category": "web",
        "tags": ["web app", "no build"],
        "langs": [
            {"id": "js", "label": "Vanilla JS", "code": """<!-- index.html \u2014 open directly in a browser, no server needed -->
<div id="app"></div>
<script>
// \u2500\u2500 STATE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const state = { items: [] };   // TODO: shape this to your data

// \u2500\u2500 RENDER \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function render() {
  const app = document.getElementById('app');
  app.innerHTML = `
    <h1>My App</h1>
    <button data-action="add">Add item</button>
    <ul>
      ${state.items.map((item, i) =>
        `<li>${item} <button data-action="remove" data-index="${i}">x</button></li>`
      ).join('')}
    </ul>
  `;
}

// \u2500\u2500 EVENTS (delegated \u2014 survives re-renders) \u2500
document.getElementById('app').addEventListener('click', (e) => {
  const action = e.target.dataset.action;
  if (action === 'add') {
    state.items.push(`Item ${state.items.length + 1}`);
    render();
  }
  if (action === 'remove') {
    state.items.splice(Number(e.target.dataset.index), 1);
    render();
  }
});

render();
</script>"""},
            {"id": "python", "label": "Python (Flask)", "code": """from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# \u2500\u2500 STATE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
state = {"items": []}   # TODO: shape this to your data

PAGE = \"\"\"
<h1>My App</h1>
<button onclick="addItem()">Add item</button>
<ul id="list"></ul>
<script>
async function refresh() {
  const res = await fetch('/items');
  const data = await res.json();
  document.getElementById('list').innerHTML =
    data.items.map((item, i) => `<li>${item} <button onclick="removeItem(${i})">x</button></li>`).join('');
}
async function addItem() { await fetch('/items', { method: 'POST' }); refresh(); }
async function removeItem(i) { await fetch(`/items/${i}`, { method: 'DELETE' }); refresh(); }
refresh();
</script>
\"\"\"

@app.route("/")
def index():
    return render_template_string(PAGE)

@app.route("/items", methods=["GET", "POST"])
def items():
    if request.method == "POST":
        state["items"].append(f"Item {len(state['items']) + 1}")
    return jsonify(state)

@app.route("/items/<int:i>", methods=["DELETE"])
def remove_item(i):
    if 0 <= i < len(state["items"]):
        state["items"].pop(i)
    return jsonify(state)

if __name__ == "__main__":
    app.run(debug=True)"""},
        ],
    },
    {
        "slug": "live-search",
        "title": "Debounced Live Search / Filter",
        "summary": "Filters a list as the user types without hammering re-renders on every keystroke.",
        "category": "web",
        "tags": ["web app", "no build"],
        "langs": [
            {"id": "js", "label": "Vanilla JS", "code": """<!-- index.html \u2014 open directly in a browser, no server needed -->
<input id="search" placeholder="Search..." />
<ul id="results"></ul>
<script>
// \u2500\u2500 DATA \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const items = ["Apple", "Banana", "Cherry"];   // TODO: your real data

// \u2500\u2500 DEBOUNCE HELPER \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

function render(list) {
  document.getElementById('results').innerHTML =
    list.map(item => `<li>${item}</li>`).join('');
}

const onSearch = debounce((query) => {
  const filtered = items.filter(i =>
    i.toLowerCase().includes(query.toLowerCase())
  );
  render(filtered);   // TODO: replace with your real filtering logic
}, 200);

document.getElementById('search').addEventListener('input', (e) => {
  onSearch(e.target.value);
});

render(items);
</script>"""},
            {"id": "python", "label": "Python (Flask)", "code": """from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# \u2500\u2500 DATA \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
ITEMS = ["Apple", "Banana", "Cherry"]   # TODO: your real data

PAGE = \"\"\"
<input id="search" placeholder="Search..." />
<ul id="results"></ul>
<script>
let timer;
document.getElementById('search').addEventListener('input', (e) => {
  clearTimeout(timer);
  timer = setTimeout(() => search(e.target.value), 200);
});
async function search(query) {
  const res = await fetch(`/search?q=${encodeURIComponent(query)}`);
  const data = await res.json();
  document.getElementById('results').innerHTML =
    data.items.map(i => `<li>${i}</li>`).join('');
}
search('');
</script>
\"\"\"

@app.route("/")
def index():
    return render_template_string(PAGE)

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    matches = [i for i in ITEMS if query in i.lower()]   # TODO: replace with your real logic
    return jsonify({"items": matches})

if __name__ == "__main__":
    app.run(debug=True)"""},
        ],
    },
    {
        "slug": "api-data-fetcher",
        "title": "API Data Fetcher \u2014 Loading & Error States",
        "summary": "The three-state fetch pattern every UI needs: loading, error, and success, handled once.",
        "category": "web",
        "tags": ["web app", "API"],
        "langs": [
            {"id": "js", "label": "Vanilla JS", "code": """<!-- index.html \u2014 open directly in a browser, no server needed -->
<div id="app"></div>
<script>
// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const API_URL = "https://api.example.com/data";   // TODO: your endpoint

const state = { status: "loading", data: null, error: null };

function render() {
  const app = document.getElementById('app');
  if (state.status === "loading") {
    app.innerHTML = "<p>Loading...</p>";
  } else if (state.status === "error") {
    app.innerHTML = `<p>Something went wrong: ${state.error}</p>`;
  } else {
    // TODO: replace with your real rendering
    app.innerHTML = `<pre>${JSON.stringify(state.data, null, 2)}</pre>`;
  }
}

async function load() {
  state.status = "loading";
  render();
  try {
    const res = await fetch(API_URL);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    state.data = await res.json();
    state.status = "success";
  } catch (err) {
    state.error = err.message;
    state.status = "error";
  }
  render();
}

load();
</script>"""},
            {"id": "python", "label": "Python (requests)", "code": """import requests
import time

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
API_URL = "https://api.example.com/data"   # TODO: your endpoint
MAX_RETRIES = 3
RETRY_DELAY = 1.5   # seconds

def load(url):
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            last_error = e
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(RETRY_DELAY)
    raise RuntimeError(f"Giving up after {MAX_RETRIES} attempts: {last_error}")

if __name__ == "__main__":
    try:
        data = load(API_URL)
        print(data)   # TODO: replace with your real handling
    except RuntimeError as e:
        print(f"Error: {e}")"""},
        ],
    },
    {
        "slug": "rest-api-starter",
        "title": "REST API Starter",
        "summary": "Basic CRUD endpoints wired up and ready to point at a real data store.",
        "category": "backend",
        "tags": ["backend", "API"],
        "langs": [
            {"id": "python", "label": "Python (FastAPI)", "code": """from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# \u2500\u2500 MODEL \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
class Item(BaseModel):
    name: str          # TODO: shape this to your data

db: list[Item] = []

@app.get("/items")
def list_items():
    return db

@app.post("/items")
def create_item(item: Item):
    db.append(item)
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id >= len(db):
        raise HTTPException(status_code=404, detail="Not found")
    return db[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id >= len(db):
        raise HTTPException(status_code=404, detail="Not found")
    return db.pop(item_id)

# Run with: uvicorn main:app --reload"""},
            {"id": "js", "label": "Node (Express)", "code": """const express = require('express');
const app = express();
app.use(express.json());

// \u2500\u2500 STATE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
let items = [];   // TODO: shape this to your data

app.get('/items', (req, res) => {
  res.json(items);
});

app.post('/items', (req, res) => {
  const item = req.body;   // TODO: validate
  items.push(item);
  res.status(201).json(item);
});

app.get('/items/:id', (req, res) => {
  const item = items[req.params.id];
  if (!item) return res.status(404).json({ error: 'Not found' });
  res.json(item);
});

app.delete('/items/:id', (req, res) => {
  if (!items[req.params.id]) return res.status(404).json({ error: 'Not found' });
  const [removed] = items.splice(req.params.id, 1);
  res.json(removed);
});

app.listen(3000, () => console.log('Listening on :3000'));"""},
        ],
    },
    {
        "slug": "websocket-server",
        "title": "Realtime WebSocket Server",
        "summary": "Broadcasts every message to all connected clients \u2014 the base for chat, multiplayer, or live dashboards.",
        "category": "backend",
        "tags": ["backend", "realtime"],
        "langs": [
            {"id": "python", "label": "Python (websockets)", "code": """import asyncio
import websockets

# \u2500\u2500 STATE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            # TODO: replace with your real message handling
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())"""},
            {"id": "js", "label": "Node (ws)", "code": """const { WebSocketServer } = require('ws');
const wss = new WebSocketServer({ port: 8765 });

// \u2500\u2500 STATE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const clients = new Set();

wss.on('connection', (ws) => {
  clients.add(ws);

  ws.on('message', (data) => {
    // TODO: replace with your real message handling
    for (const client of clients) {
      if (client !== ws) client.send(data.toString());
    }
  });

  ws.on('close', () => clients.delete(ws));
});

console.log('WebSocket server on :8765');"""},
        ],
    },
    {
        "slug": "sqlite-persistence",
        "title": "SQLite Persistence Layer",
        "summary": "A tiny data layer with a real table and connection handling, so you stop losing state on restart.",
        "category": "backend",
        "tags": ["backend", "database"],
        "langs": [
            {"id": "python", "label": "Python (sqlite3)", "code": """import sqlite3

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
DB_PATH = "app.db"   # TODO: your database file

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute(\"\"\"
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        \"\"\")   # TODO: shape this to your data

def add_item(name):
    with get_connection() as conn:
        cur = conn.execute("INSERT INTO items (name) VALUES (?)", (name,))
        return cur.lastrowid

def list_items():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM items").fetchall()
        return [dict(row) for row in rows]

def delete_item(item_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM items WHERE id = ?", (item_id,))

if __name__ == "__main__":
    init_db()
    add_item("Example")   # TODO: replace with your real logic
    print(list_items())"""},
            {"id": "js", "label": "Node (better-sqlite3)", "code": """const Database = require('better-sqlite3');

// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const DB_PATH = 'app.db';   // TODO: your database file

const db = new Database(DB_PATH);

function initDb() {
  db.exec(`
    CREATE TABLE IF NOT EXISTS items (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL
    )
  `);   // TODO: shape this to your data
}

function addItem(name) {
  const stmt = db.prepare('INSERT INTO items (name) VALUES (?)');
  const info = stmt.run(name);
  return info.lastInsertRowid;
}

function listItems() {
  return db.prepare('SELECT * FROM items').all();
}

function deleteItem(id) {
  db.prepare('DELETE FROM items WHERE id = ?').run(id);
}

initDb();
addItem('Example');   // TODO: replace with your real logic
console.log(listItems());"""},
        ],
    },
    {
        "slug": "file-watcher",
        "title": "File Watcher & Automation",
        "summary": "Watches a folder and fires your own logic on any create, edit, or delete.",
        "category": "tooling",
        "tags": ["automation", "tooling"],
        "langs": [
            {"id": "python", "label": "Python", "code": """import time
import os

# \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
WATCH_DIR = "./watched"     # TODO: folder to watch
POLL_SECONDS = 2

def on_change(filename, event):
    # TODO: replace with your real action
    print(f"[{event}] {filename}")

def watch():
    os.makedirs(WATCH_DIR, exist_ok=True)
    seen = {f: os.path.getmtime(os.path.join(WATCH_DIR, f))
            for f in os.listdir(WATCH_DIR)}

    while True:
        time.sleep(POLL_SECONDS)
        current = os.listdir(WATCH_DIR)

        for f in current:
            path = os.path.join(WATCH_DIR, f)
            mtime = os.path.getmtime(path)
            if f not in seen:
                on_change(f, "created")
            elif mtime != seen[f]:
                on_change(f, "modified")
            seen[f] = mtime

        for f in list(seen):
            if f not in current:
                on_change(f, "deleted")
                del seen[f]

if __name__ == "__main__":
    watch()"""},
            {"id": "js", "label": "Node", "code": """const fs = require('fs');
const path = require('path');

// \u2500\u2500 CONFIG \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const WATCH_DIR = './watched';   // TODO: folder to watch

fs.mkdirSync(WATCH_DIR, { recursive: true });

function onChange(filename, eventType) {
  // TODO: replace with your real action
  console.log(`[${eventType}] ${filename}`);
}

fs.watch(WATCH_DIR, (eventType, filename) => {
  if (filename) onChange(filename, eventType);
});

console.log(`Watching ${path.resolve(WATCH_DIR)}...`);"""},
        ],
    },
    {
        "slug": "cli-tool",
        "title": "CLI Tool Starter",
        "summary": "Argument parsing, verbose flag, and file output already wired up.",
        "category": "tooling",
        "tags": ["CLI", "tooling"],
        "langs": [
            {"id": "python", "label": "Python", "code": """import argparse

def main():
    parser = argparse.ArgumentParser(description="TODO: describe your tool")
    parser.add_argument("input", help="Input file or value")
    parser.add_argument("-o", "--output", default=None, help="Output path")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print(f"Processing: {args.input}")

    result = process(args.input)   # TODO: your real logic

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
    else:
        print(result)

def process(value):
    return value.upper()   # TODO: replace

if __name__ == "__main__":
    main()"""},
            {"id": "js", "label": "Node", "code": """#!/usr/bin/env node
const args = process.argv.slice(2);

// \u2500\u2500 PARSE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
const input = args[0];
const verbose = args.includes('-v') || args.includes('--verbose');
const outIndex = args.findIndex(a => a === '-o' || a === '--output');
const output = outIndex !== -1 ? args[outIndex + 1] : null;

if (!input) {
  console.error('Usage: mytool <input> [-o output] [-v]');
  process.exit(1);
}

if (verbose) console.error(`Processing: ${input}`);

const result = transform(input);   // TODO: your real logic

if (output) {
  require('fs').writeFileSync(output, result);
} else {
  console.log(result);
}

function transform(value) {
  return value.toUpperCase();   // TODO: replace
}"""},
        ],
    },
    {
        "slug": "scheduled-task-runner",
        "title": "Scheduled Task Runner",
        "summary": "Runs jobs on a recurring schedule without cron or a task scheduler service.",
        "category": "tooling",
        "tags": ["automation", "tooling"],
        "langs": [
            {"id": "python", "label": "Python", "code": """import time
import schedule   # pip install schedule

# \u2500\u2500 JOBS \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
def job():
    # TODO: replace with your real task
    print("Running scheduled job...")

# \u2500\u2500 SCHEDULE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
schedule.every(1).hours.do(job)          # TODO: adjust interval
schedule.every().day.at("09:00").do(job) # TODO: or use a fixed time

if __name__ == "__main__":
    print("Scheduler started, waiting for jobs...")
    while True:
        schedule.run_pending()
        time.sleep(1)"""},
            {"id": "js", "label": "Node", "code": """const cron = require('node-cron');   // npm install node-cron

// \u2500\u2500 JOBS \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function job() {
  // TODO: replace with your real task
  console.log('Running scheduled job...');
}

// \u2500\u2500 SCHEDULE \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
cron.schedule('0 * * * *', job);     // TODO: adjust \u2014 this runs hourly
cron.schedule('0 9 * * *', job);     // TODO: or a fixed daily time

console.log('Scheduler started, waiting for jobs...');"""},
        ],
    },
]

CATEGORY_LABELS = {
    "hardware": "Hardware",
    "backend": "Backend",
    "web": "Web",
    "tooling": "Tooling",
}
