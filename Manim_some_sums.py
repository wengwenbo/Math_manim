from manim import *
class Formula(Scene):
    def consturct(self):
        Euler_Formula=Tex(r"$(\text{e}^{\frac{\text{i}m\pi}{2n}})^{2n}=\text{e}^{\text{i}m\pi}=(-1)^m(m=1,2,...n)$")
        DeM_Formula=Tex(r"$\text{e}^{\text{i}m\pi}=(\cos\frac{m\pi}{2n}+\text{i}\sin\frac{m\pi}{2n})^{2n}=\cos m\pi+\text{i}\sin m\pi$")