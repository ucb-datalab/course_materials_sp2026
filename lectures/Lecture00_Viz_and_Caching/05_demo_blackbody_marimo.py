import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Interactive Blackbody Animation

        This notebook uses widgets to illustrate blackbody temperature.

        $$B_\nu(T) = \frac{2h\nu^2}{c^3}\frac{1}{e^\frac{h\nu}{k_BT} - 1}$$

        $$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\frac{1}{e^\frac{hc}{\lambda k_BT} - 1}$$
        """
    )
    return


@app.cell
def _(np):
    # High-level parameters
    SIZE = 2048     # number of points in each line
    LAM_MIN = -8
    LAM_MAX = 0
    NU_MIN = 10 - LAM_MAX
    NU_MAX = 10 - LAM_MIN

    # Constants
    h = 6e-27  # erg s
    c = 3e10  # cm / s
    k_B = 1.3e-16  # erg / K

    # Variables derived from parameters above
    nus = np.logspace(NU_MIN, NU_MAX, SIZE)
    lam = np.logspace(LAM_MIN, LAM_MAX, SIZE)

    # Wavelength bands
    RP = (640e-7, 1050e-7)  # cm
    BP = (330e-7, 680e-7)  # cm
    return BP, LAM_MAX, LAM_MIN, NU_MAX, NU_MIN, RP, SIZE, c, h, k_B, lam, nus


@app.cell
def _(mo):
    # Temperature slider
    temp_slider = mo.ui.slider(
        start=3.0,
        stop=5.0,
        step=0.1,
        value=3.0,
        label="Log₁₀ Temperature [K]",
        show_value=True,
    )
    temp_slider
    return (temp_slider,)


@app.cell
def _(BP, RP, c, h, k_B, lam, np, nus, plt, temp_slider):
    # Get temperature from slider
    T = 10 ** temp_slider.value

    # Calculate blackbody spectra
    y_n = 2 * h * nus**3 / c**2 / (np.exp(h * nus / (k_B * T)) - 1)
    y_l = 2 * h * c**2 / lam**5 / (np.exp(h * c / (lam * k_B * T)) - 1)

    # Create figure
    fig, ax = plt.subplots(ncols=2, figsize=(10, 4))

    # Configure axes
    for _ax in ax:
        _ax.grid(True)
        _ax.set_yscale('log')
        _ax.set_xscale('log')

    # Left plot: B_nu
    ax[0].plot(nus, y_n, 'k')
    ax[0].axvspan(c / RP[1], c / RP[0], color='red', alpha=0.3)
    ax[0].axvspan(c / BP[1], c / BP[0], color='blue', alpha=0.3)
    ax[0].set_title(r'$B_\nu$')
    ax[0].set_xlabel('Frequency [Hz]')
    ax[0].set_ylabel('Specific Intensity [erg s⁻¹ cm⁻² sr⁻¹ Hz⁻¹]')
    ax[0].set_ylim(1e-25, 1e0)

    # Right plot: B_lambda
    ax[1].plot(lam, y_l, 'k')
    ax[1].axvspan(RP[0], RP[1], color='red', alpha=0.3)
    ax[1].axvspan(BP[0], BP[1], color='blue', alpha=0.3)
    ax[1].set_title(r'$B_\lambda$')
    ax[1].set_xlabel('Wavelength [cm]')
    ax[1].set_ylabel('Specific Intensity [erg s⁻¹ cm⁻³ sr⁻¹]')
    ax[1].set_ylim(1e0, 1e25)

    plt.tight_layout()
    fig
    return T, ax, fig, y_l, y_n


if __name__ == "__main__":
    app.run()
