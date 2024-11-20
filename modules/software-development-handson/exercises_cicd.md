---
title: CI/CD optimization
type: exercise
order: 4
---

# Make your automated testing framework use less energy

## Testing is necessary
A robust testing framework is an essential part of good software development practices. It is even more vital in a research environment since wrong or misleading scientific results may be caused by bad or insufficient testing. Automated testing aids in scientific reproducibility and reduces the amount of time wasted trying to go back to find which version still worked with a given feature.

If you are unsure about what a testing framework is or how to set one up, you can learn about it in the [Good Practices](exercises_good-practices) exercises of this hands-on module (specifically, it is [step 4](exercises_good-practices#_4-testing). Adding tests to your scientific code is a good step towards avoiding wasted energy in the long run.


## Testing uses energy
Despite the need for it, testing necessarily uses energy. By adding a testing suite to your software you are making the value judgement that the benefits are worth the additional energy cost of running automatic tests.

But there are ways to mimimize the amount of energy used.
The defaults used by most people when adding automated tests to their code base are often wasteful, due to many tests being run when it is not necessary.

## Reduce energy waste from unnecessary testing
In the following we address some relatively simple changes that can be made to reduce the unnecessary runnng of tests.
The solutions are given for projects that use `pytest` (the ubiquitous python testing framework) and automation using features of [GitHub](www.github.com), which is a very common place to host code repositories. However, if you are using a different language (e.g. `R`) or you do not use GitHub (maybe GitLab, bitbucket etc) then the general principle should still apply. It may be possible to recreate the same changes by modifying the relevant configuration (we will try to help where we can).

### 1. Cancel running workflows on a new push
By default, it is often the case that currently running tests continue to completion, even if you have pushed new changes to the branch. While that may be desirable in some cases, it is most often not wanted. The user is most interested in whether the newest version of a branch is passing the tests or not.

Luckily, it is possible to [automatically cancel running tests if new code is pushed to the branch](https://docs.github.com/en/enterprise-cloud@latest/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs#example-using-concurrency-and-the-default-behavior).

### 2. Only re-run tests that failed
Use the `pytest --last-failed` command by exploiting the gh actions cache functionality using a ready-made github action:
* pytest-last-failed: <https://github.com/sjvrijn/pytest-last-failed>

### 3. Set the workflow trigger appropriately for each part of the test framework
Test workflows are triggered to run when a particular event happens. To avoid tests running unnecessarily, it is important to ensure that this trigger is set correctly.

Certain test workflows do not need to run on every push, for example, and could be configured to only run on merges to the main branch (or on tagging releases).

[GitHub docs on triggering workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)


### 4. Test on different platforms/versions that make sense
It is possible to run your automated tests on several platforms (e.g. different versions of Ubuntu, MacOS and Windows) and also on different kinds of software stack (different libraries, `python` versions etc.). On GitHub, for example, this can be done using [`matrix` strategies](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow). This is generally desirable, in order to ensure portability across systems.

However, testing all these combinations comes at a cost. It is important to think about how many users you have (maybe it is just you and some colleagues) and whether what you are testing is actually necessary. For example, supporting every python version from the last 10 years is probably overkill and will waste a lot of energy.


### 5. Create dependencies between tests

Continuing to run all tests when one has failed does not always make sense. For example, if a basic linting step has failed, it may be desirable not to run the remaining test suite until that is fixed.

With GitHub actions this is possible by making dependencies between your jobs: [see relevant example here](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#example-requiring-successful-dependent-jobs).

Alterntively, you may wish to only run the linting tests once the basic tests pass (i.e. no point linting broken code). Which way of adding dependencies is best at reducing unnecessary tests running is dependent on your specific setup.


### Other tools/plugins worth a look

A possible alternative to `pytest-last-failed`:
* pytest-testmon: <https://github.com/tarpas/pytest-testmon>, a pytest plugin that only runs tests that concern code that has been affected by changes (interesting but challenging, and possibly unreliable)


## Conclusion
Testing is essential to reducing waste in research software development, but can cause significant energy consumption itself. This is due to the way most testing frameworks are by default configured to run all of the tests, all of the time. By following some or all of the above changes, you can likely save energy by reducing a lot of pointless tests being run.

