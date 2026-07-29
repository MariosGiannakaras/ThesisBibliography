## SRC-495952EBB9 — Make your own custom environment - Gymnasium Documentation

- **Priority:** P2-supporting
- **Topics:** gridworld, benchmark-tooling
- **Source:** https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation
- **Markdown:** `sources/markdown/SRC-495952EBB9__make-your-own-custom-environment-gymnasium-documentation.md`
- **Review status:** machine-selected; full-text verification pending

> - Our custom environment will inherit from the abstract class `gymnasium.Env` . You shouldn't forget to add the `metadata` attribute to your class. There, you should specify the render-modes that are supported by your environment (e.g., `"human"` , `"rgb_array"` , `"ansi"` ) and the framerate at which your environment should be rendered. Every environment should support `None` as render-mode; you don't need to add it in the metadata. In `GridWorldEnv` , we will support the modes “rgb_array” and “human” and render at 4 FPS.
