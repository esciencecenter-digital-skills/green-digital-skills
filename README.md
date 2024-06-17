# Green Digital Skills
This repository contains the contents for the Green Digital Skills lesson material. This is intended to raise awareness of environmental issues relating to research computing, providing some best practices in green coding and exploring a range of solutions to profile and reduce energy usage for different kinds of common workflows.

The website with this lesson material can be found here: <https://esciencecenter-digital-skills.github.io/green-digital-skills/>

## Target audience
The current lesson material is being developed for a pilot workshop at the Prinses Máxima Centrum.

## Technical documentation
This platform uses the [NEBULA framework](https://github.com/esciencecenter-digital-skills/NEBULA).

For elaborate setup instructions and other documentation, see the [NEBULA documentation](https://github.com/esciencecenter-digital-skills/NEBULA-docs)

## Quick local setup

More detailed information about local setup can be found in the [NEBULA local rendering docs](https://github.com/esciencecenter-digital-skills/NEBULA-docs/blob/main/local-rendering.md)

### Content directory/repository

To use NEBULA to build the content in this repository locally, you will need to clone this repository and the NEBULA repository:

```bash
git clone git@github.com:esciencecenter-digital-skills/green-digital-skills.git
git clone git@github.com:esciencecenter-digital-skills/NEBULA.git
```

### Link to the content repository

To make sure that NEBULA knows where to find the content, we create the following environment variable:

```bash
export CONTENT_PATH="~/path/to/your/content/repository"
```

### Install dependencies

Install the dependencies using the [node package manager](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```bash
# node package manager
npm install
```

### Local development build

Start the development server on `http://localhost:3000`:

```bash
# node package manager
npm run dev
```

Now you can open a browser and navigate to `http://localhost:3000/green-digital-skills`
