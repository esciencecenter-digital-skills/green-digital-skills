# NEBULA-content-template
This template repository can be used to create an easily maintainable, version-controllable, web-based lesson collection to be deployed with the [NEBULA framework](https://github.com/esciencecenter-digital-skills/NEBULA).

## Repo instantiation
To create a custom-made lesson repository, click the `Use this template` button located at the top right of this page.

## Configure GitHub Pages
After instantiation, you need to set up your repo's GitHub Pages. Follow these steps:
- Go to `Settings` (located on the top toolbar), and then click on `Pages`.
- Under the `Branch` option, select the `gh-pages` branch and then click `Save`. Use the `/root` folder as the default.
- Return to your main repository page.
- In the `About` section of your repository details, find the `Website` field and select `Use your GitHub Pages website`.

## Add the title of your lesson and additional sections
This can be configured through the `config.json` file. Below is an example of its contents:
```
{
  "publicProps": {
    "title": "Add a title for your lesson/project",
    "baseURL": "NEBULA-content-template",
    "repoName": "NEBULA-content-template",
    "repoOwner": "esciencecenter-digital-skills",
    "organization": "Netherlands eScience Center",
    "categoryOrder": ["Category1", "Category2"]
  }
}
```
You can modify the `"title"` field to reflect your specific topic and add new sections to your lesson under `"categoryOrder"`.

The `"repoName"` and `"baseURL"` fields are automatically updated to the name of your new repository using the [generate_config.yml](https://github.com/esciencecenter-digital-skills/NEBULA-content-template/blob/main/.github/workflows/generate_config.yml) file. The corresponding workflow is triggered only once upon repository instantiation and is subsequently disabled.

## Adding new modules
This repository includes dummy model modules as templates that you can follow to create your own modules. Please, follow the recommended formats and file extensions.
See also [NEBULA-docs](https://github.com/esciencecenter-digital-skills/NEBULA-docs) for information on how to create new modules.

## Suggestions and further info
Suggestions are always welcome.
For this and any other issues, we invite you contribute to the project by creating `Issues` and `Pull requests`.
If needed, you can also contact us directly:
- Carlos M. R. Rocha: c.rocha@esciencecenter.nl
- Jaro Camphuijsen: j.camphuijsen@esciencecenter.nl
- Robin Richardson: r.richardson@esciencecenter.nl


