# Did the robot finish the task?

An eight-case **symbolic frame fixture** inspired by Instance's [task-and-video success verifier](https://www.instancelabs.ai/) and [YC launch](https://www.ycombinator.com/companies/most-robotic). It asks whether “success at any point” means “success at the end.” No videos, robot, model, or Instance API are used.

Run `python3 experiment.py`. The task is “put the object in the bin and finish with the drawer closed.” Each frame records whether both conditions are true (`T`), false (`F`), or not visible (`?`). The script compares an any-frame success rule with a terminal-evidence rule that can abstain.

The two rules disagree on **5 of 8 hand-authored episodes**; terminal evidence returns **unknown on 2**. Transient success, reopening a drawer, removing an object, and final occlusion expose different reasons. The counts measure this fixture only. They do not estimate Instance's classifier accuracy. The next experiment would pair real labeled videos with task-specific evidence requirements, measure false success and abstention rates, and compare final-frame versus temporal judgments across camera angles.

Sources: [Instance site](https://www.instancelabs.ai/), [verifier demo and output contract](https://demo.instancelabs.ai/), [YC profile](https://www.ycombinator.com/companies/most-robotic).
