<div align='center'>
    <img src='readme/icon.png' width='200'/>
    <h2>🛰️ N2YO.com Python API Wrapper</h2>
</div>

<p align='center'>
  <p align='center'>
    <a href='https://github.com/g1ampy/n2yo-api-wrapper/stargazers'><img alt='Stars' src='https://img.shields.io/github/stars/g1ampy/n2yo-api-wrapper?color=blue'/></a>
    <a href='https://github.com/g1ampy/n2yo-api-wrapper/forks'><img alt='Forks' src='https://img.shields.io/github/forks/g1ampy/n2yo-api-wrapper?color=blue'/></a>
    <a href='https://github.com/g1ampy/n2yo-api-wrapper/releases'><img alt='GitHub release' src='https://img.shields.io/github/v/release/g1ampy/n2yo-api-wrapper?color=blue'/></a>
    <a href='https://github.com/g1ampy/n2yo-api-wrapper/blob/main/LICENSE'><img alt='License' src='https://img.shields.io/github/license/g1ampy/n2yo-api-wrapper?color=blue'/></a>
    <a href='https://pypi.org/project/n2yo-api.wrapper/'><img alt='PyPI' src='https://img.shields.io/pypi/v/n2yo-api-wrapper?color=blue'></a>
    </p>
</p>


<p align='center'> A lightweight, feature-complete Python interface for satellite tracking using N2YO.com's API </p>

### 🛰️ About The Project

A Pythonic interface for accessing real-time satellite data from [N2YO.com](https://www.n2yo.com/api/). This wrapper simplifies interactions with the N2YO API by handling authentication, request formatting, error handling, and response parsing - transforming JSON payloads into native Python objects.


### ✨ Key Features
- **Real-time Satellite Tracking**: Get current position and trajectory data
- **Pass Prediction**: Calculate visible passes for any location
- **TLE Data Access**: Retrieve latest orbital parameters
- **Satellite Search**: Find satellites by name/category
- **Type Annotations**: Full IDE support and type safety

### ⚙️ Installation
```bash
pip install n2yo-api-wrapper
```

### 🔑 API Key Setup
  1. **Get a free API key from N2YO.com**
  2. **Setup client**
```python
from n2yo import n2yo
client = n2yo(api_key="YOUR_API_KEY")'
```

### 🚀 Usage Examples

```python
from n2yo import n2yo

# Initialize client
client = n2yo(api_key="YOUR_API_KEY")

# Get satellite positions
positions = client.get_satellite_positions(25544, 41.702, -76.014, 500, 10)

# Predict visible passes
passes = client.get_visual_passes(25544, 41.702, -76.014, 500, 3)

# Retrieve TLE data
tle = client.get_tle(25544)

# Return all objects within a given search radius above observer's location
above = client.get_above(41.702, -76.014, 0, 70, 18)
```

### 📜 Error Handling
- **N2YOInvalidKeyException:** Invalid API key.
```python
try:
    data = client.get_positions(...)
except N2YOInvalidKeyException:
    print("Invalid API key configured")
```

### 📚 Full Method Reference
[Please refer to the full documentation](https://www.n2yo.com/api/)

### 📃 License

This project is licensed under the [MIT License](./LICENSE.txt).

### 👨‍💻 Our Contributors

<a href='https://github.com/g1ampy/n2yo-api-wrapper/graphs/contributors'>
    <img src='https://contrib.rocks/image?repo=g1ampy/n2yo-api-wrapper'>
</a>