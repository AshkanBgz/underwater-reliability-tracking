# Reliability-aware underwater feature tracking

MSc AI dissertation (Computing Research Project, 55-710244-AF), Sheffield Hallam University.

The question is when an underwater robot should trust its normal camera frames and when it
should switch to event-camera data instead. On the AquaticVision dataset I build grayscale
frames and three event representations (time surface, event-count image, voxel grid) for
short time windows, run the same feature tracker on each, and then train simple models to
predict which input will track best from quality features of the window. If nothing looks
reliable, the selector can refuse to pick anything.

This is work in progress and follows the project delivery plan task by task.


```
py -3.10 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Layout

- `src/` reusable code (reading bags, event representations, tracker)
- `scripts/` small scripts, named after the plan task they belong to
- `scripts/learn/` the first exploration scripts I wrote to understand the data
- `results/` output tables (big figures are not committed)
- `docs/` notes, dataset audit, data-quality report, data dictionary
