<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![PyPi][pypi-shield]][pypi-url]
[![MIT][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/g1ampy/n2yo-api-wrapper">
    <img src="images/logo.png" alt="Logo" width="400">
  </a>

<h3 align="center">N2YO.com API Wrapper</h3>

  <p align="center">
    A lightweight and easy-to-use Python wrapper for the N2YO.com API
    <br />
    <a href="https://github.com/g1ampy/n2yo-api-wrapper"><strong>« Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/g1ampy/n2yo-api-wrapper/issues/new?labels=bug&template=bug-report---.yml">Report Bug</a>
    &middot;
    <a href="https://github.com/g1ampy/n2yo-api-wrapper/issues/new?labels=enhancement&template=feature-request---.yml">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## ℹ️ About The Project

The N2YO API Wrapper is a Python tool designed to interact with the N2YO satellite tracking API. It simplifies API requests, handles API keys and parses JSON responses into structured Python objects, providing methods to fetch real-time satellite positions, visible passes and orbital data. This makes it easy for developers to quickly and efficiently integrate satellite tracking and space data into their applications.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]
[![requests][requests]][requests-url]
[![dacite][dacite]][dacite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## 🟢 Getting Started

To use the N2YO.com API Wrapper you can clone the repository or use `pip` package (recommended)

### Prerequisites

- Python 3.10 or higher  
- A free API key from [https://www.n2yo.com](https://www.n2yo.com)

### Installation
```sh
pip install n2yo-api-wrapper
```

<p align="right">(<a href="#readme-top">back to top ⬆️</a>)</p>



<!-- USAGE EXAMPLES -->
## ❓ Usage

Here’s a basic example of how to use the N2YO API wrapper to track a satellite (e.g., the ISS):

```python
from n2yo import n2yo

# Initialize the API client with your key
wrapper = n2yo(api_key="YOUR_API_KEY")

# Get real-time position of the ISS (satellite ID: 25544)
position = wrapper.get_satellite_positions(
    id=25544,              
    observer_lat=41.9028,   # Latitude (e.g., Rome)
    observer_lng=12.4964,   # Longitude
    observer_alt=100,       # Altitude in meters
    seconds=1
)

print(position)
```

### 📌 Available Methods

- `get_satellite_positions(...)` – Get current position of a satellite
- `get_tle(satellite_id)` – Retrieve the TLE data
- `get_visual_passes(...)` – Get upcoming visible passes
- `get_radio_passes(...)` – Get upcoming radio passes
- `get_above(...)` – List satellites currently above a location

_For more examples, please refer to the [Documentation](https://www.n2yo.com/api/)_

<p align="right">(<a href="#readme-top">back to top ⬆️</a>)</p>



<!-- CONTRIBUTING -->
## 🌱 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top ⬆️</a>)</p>



### Top contributors:

<a href="https://github.com/g1ampy/n2yo-api-wrapper/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=g1ampy/n2yo-api-wrapper" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## 📜 License

Distributed under the MIT. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top ⬆️</a>)</p>



<!-- CONTACT -->
## 📥 Contact

<a href="mailto:g1ampy@proton.me">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
</a>

<p align="right">(<a href="#readme-top">back to top ⬆️</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/g1ampy/n2yo-api-wrapper.svg
[contributors-url]: https://github.com/g1ampy/n2yo-api-wrapper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/g1ampy/n2yo-api-wrapper.svg
[forks-url]: https://github.com/g1ampy/n2yo-api-wrapper/network/members
[stars-shield]: https://img.shields.io/github/stars/g1ampy/n2yo-api-wrapper.svg
[stars-url]: https://github.com/g1ampy/n2yo-api-wrapper/stargazers
[issues-shield]: https://img.shields.io/github/issues/g1ampy/n2yo-api-wrapper.svg
[issues-url]: https://github.com/g1ampy/n2yo-api-wrapper/issues
[pypi-shield]: https://img.shields.io/pypi/v/n2yo-api-wrapper
[pypi-url]: https://pypi.org/project/n2yo-api-wrapper/
[license-shield]: https://img.shields.io/github/license/g1ampy/n2yo-api-wrapper.svg
[license-url]: https://github.com/g1ampy/n2yo-api-wrapper/blob/stable/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[dacite]: https://img.shields.io/badge/dacite-20232A?style=for-the-badge&logo=github&logoColor=61DAFB
[dacite-url]: https://github.com/konradhalas/dacite
[requests]: https://img.shields.io/badge/requests-35495E?style=for-the-badge&logo=github&logoColor=4FC08D
[requests-url]: https://github.com/psf/requests