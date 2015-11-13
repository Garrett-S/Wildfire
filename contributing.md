CONTRIBUTING
============

For development of the Wildfire system we will be using a git workflow
(https://git-scm.com/) via github (https://github.com/). Our repository is
located at https://github.com/matthewrsj/Wildfire.

Git is an open source version control system that decentralizes your code base.
Git uses branching and merging to allow multiple users to modify the same code.
Developers can save their changes in manageable blocks called commits to allow
for history review and revision. A typical workflow may look like the following
using Github:

* Issue is created in the main repository (matthewrsj/Wildfire) to address a
  specific task of a specific user story. This issue is assigned to a pair of
  developers.
* The assigned developers fork (https://help.github.com/articles/fork-a-repo/)
  the main repository and modify the code to fix the issue created on the main
  repository.
  - The developers write tests to test the implementation. These tests are
    reviewed by the rest of the team to ensure proper testing.
  - The developers implement the changes to make the code pass.
  - The developers commit their changes with brief but meaningful commit
    messages to describe specific changes.
* Once the implementation passes the tests, the assigned developers open a pull
  request (https://help.github.com/articles/using-pull-requests/) to the main
  repository. This pull request is reviewed by other developers in the team and
  is either approved or suggestions are made.
  - If suggestions are made, the developers address the concerns and the review
    process starts again.
* Once the pull request is approved, it is merged and the issue is closed as
  fixed.
