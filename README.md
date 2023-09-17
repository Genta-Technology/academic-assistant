<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Genta-Technology/Academic-Assistant">
    <img src="Extension.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Genta Academic Assistant</h3>

  <p align="center">
    An AI assistant built specifically to help student and researcher with their study by giving them the precise answer based on papers on our database.
    <br />
    <a href="https://github.com/Genta-Technology/Academic-Assistant"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Genta-Technology/Academic-Assistant">View Demo</a>
    ·
    <a href="https://github.com/Genta-Technology/Academic-Assistant/issues">Report Bug</a>
    ·
    <a href="https://github.com/Genta-Technology/Academic-Assistant/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Genta Academic Assistant is an AI assistant built specifically to help student and researcher with their study by giving them the precise answer based on papers on our database. We built our app because we know how painful it is to search or find the right academic literature , quickly, and precisely for our research/courses using traditional methods; like using google scholar or a library. Unlike library's that uses filters to find papers, which sometimes can be unreliable, this app can precisely pinpoint the top papers, from the database, that is the most relevant to the prompt that is passed to it. Due to this the hustle of finding  the right research papers is reduce and will be way more easier than ever before.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Streamlit][Streamlit]][Streamlit-url]
* [![Weaviate][Weaviate]][Weaviate-url]
* [![OpenAI][OpenAI]][OpenAI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Make sure you have `>=python-3.8` installed on your machine. If you don't have it installed, you can download it [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository
    ```sh
    git clone https://github.com/Genta-Technology/Academic-Assistant.git
    ```
2. Install the dependencies
    ```sh
    pip install -r requirements.txt
    ```
3. Setup the environment variables, by copying the `.env.example` file to `.env`
    ```sh
    cp .env.example .env
    ```
    Then fill in the values in the `.env` file with your own values. For the `WEAVIATE_CLIENT_ENDPOINT`, you can use your own new database (local or cloud) in [Weaviate](Weaviate-url) and fill it up using the `database_initialization.py`, or email us at `rbisri@student.ubc.ca`.
4. Run the app
    ```sh
    streamlit run app.py
    ```

### Setup new database

Follow these setup if you want to setup a new database locally, and already followed the steps above.

1. Initialize a database
    - Locally:
        Make sure you have docker installed on your machine. If you don't have it installed, you can download it [here](https://www.docker.com/products/docker-desktop).
        ```sh
        cd database
        docker compose up -d
        ```
    - Cloud:
        Follow this [guide](https://weaviate.io/developers/wcs/quickstart) to setup a new database in the cloud.

2. Insert your database endpoint to the `.env` file
    ```sh
    WEAVIATE_CLIENT_ENDPOINT=<your_database_endpoint>
    ```

3. Download any dataset you want to use to fill up the database. For example, you can download the [arxiv dataset](https://www.kaggle.com/Cornell-University/arxiv) from Kaggle. Then, put the dataset in the `data` folder.

4. Fill up the database
    ```sh
    python database_initialization.py --data <path_to_dataset>
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Once you run the app, simply open the application on your favorite browser and fill the token input with your [OpenAI](OpenAI-url) API key. Then, you can start using the app by filling the query input with your prompt. For example, if you want to find the top papers that is the most relevant to the question `What is the best way to reduce the spread of COVID-19?`, you can fill the query input with that question and click the `Submit` button. Then, the app will try to answer your question based on the search result, and show you the top papers that is the most relevant to the prompt.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
<!-- 
- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature -->

See the [open issues](https://github.com/Genta-Technology/Academic-Assistant/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-2.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

1. Rifky Bujana Bisri - [@rifkybujanabisri](https://www.instagram.com/rifkybujanabisri/) - rbisri@student.ubc.ca
2. Alifais Farrel Ramdhani - [@farrel_ramdhani](https://www.instagram.com/farrel_ramdhani/) - alifais@student.ubc.ca
3. Evint Leovonzko - [@evint_leo](https://www.instagram.com/evint_leo/) - evintkoo@student.ubc.ca
4. Muhammad Hilmy Abdurrahim - [@mhilmya04](https://www.instagram.com/mhilmya04/) - mabdurra@student.ubc.ca

Project Link: [https://github.com/Genta-Technology/Academic-Assistant](https://github.com/Genta-Technology/Academic-Assistant)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Genta-Technology/Academic-Assistant.svg?style=for-the-badge
[contributors-url]: https://github.com/Genta-Technology/Academic-Assistant/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Genta-Technology/Academic-Assistant.svg?style=for-the-badge
[forks-url]: https://github.com/Genta-Technology/Academic-Assistant/network/members
[stars-shield]: https://img.shields.io/github/stars/Genta-Technology/Academic-Assistant.svg?style=for-the-badge
[stars-url]: https://github.com/Genta-Technology/Academic-Assistant/stargazers
[issues-shield]: https://img.shields.io/github/issues/Genta-Technology/Academic-Assistant.svg?style=for-the-badge
[issues-url]: https://github.com/Genta-Technology/Academic-Assistant/issues
[license-shield]: https://img.shields.io/github/license/Genta-Technology/Academic-Assistant.svg?style=for-the-badge
[license-url]: https://github.com/Genta-Technology/Academic-Assistant/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: Genta-Academic-Assistant-SS.png
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
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[Weaviate]: https://img.shields.io/badge/Weaviate-4432a8?style=for-the-badge&logo=weaviate&logoColor=white
[Weaviate-url]: https://weaviate.io/
[OpenAI]: https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white
[OpenAI-url]: https://openai.com/