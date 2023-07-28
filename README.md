<h1>Harmonized MIxS 6.2 Release Candidate</h1>

Documentation and data validator: http://w3id.org/mixs-6-2-rc/
- This validator does not submit data to any repository

<nav>
  <a href="https://github.com/turbomam/mixs-envo-struct-knowl-extraction">Repo</a>
  |
  <a href="https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues">Report Bug</a>
  |
  <a href="https://github.com/turbomam/mixs-envo-struct-knowl-extraction/releases">Releases</a>
</nav>

<!-- TABLE OF CONTENTS -->

<br><br>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
  </ol>
</details>
<br><br>
<!-- ABOUT THE PROJECT -->

## About The Project

This repository takes the [MIxS 6.1 Excel specification](https://github.com/GenomicsStandardsConsortium/mixs/blob/main/mixs/excel/mixs_v6.xlsx) and converts it to [LinkML](https://linkml.io/) YAML. Term elements are harmonized, 
previously informal data constraints are formalized, and validation tools are provided. For consideration as MIxS 6.2 at the 
The [23rd Genomic Standards Consortium Meeting](https://genomicsstandardsconsortium.github.io/GSC23-Bangkok/) in August 2023 in Bangkok, Thailand. Hosted by Siriraj Hospital Mahidol University and the 
National Center for Genetic Engineering and Biotechnology in Bangkok, Thailand.

<h2>And future site of MIxS/EnvO Structured Knowledge Extraction</h2>

<p>Extracting structured knowledge from MIxS and finding EnvO terms that would be reasonable answers to scoped MIxS questions</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is a standard Python project that runs on the CLI.

### Prerequisites

- python >= 3.10 (it will probably work with lower versions, but I haven't tested it)
- poetry >= 1.2

### Installation

1. Install dependencies `> poetry install`
1. Run with `> make all`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

<!-- ## Usage

[TODO] Use this space to show useful examples of how a project can be used.

<p align="right">(<a href="#readme-top">back to top</a>)</p>  -->

<!-- ROADMAP -->

See the [open issues](https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues) for a full list of proposed
features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE.md](./LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

Mark Andrew Miller, [National Microbiome Data Colalborative](https://microbiomedata.org/), Lawrence Berkeley National Laboratory
- MAM@lbl.gov

<p align="right">(<a href="#readme-top">back to top</a>)</p>
