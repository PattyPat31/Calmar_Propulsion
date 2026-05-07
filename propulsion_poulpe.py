#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Projet L1 — Propulsion d'un poulpe / méduse

Objectif :
----------
Simuler le déplacement vertical d’un animal marin
qui se propulse en éjectant de l’eau.

Le modèle est volontairement simplifié.

L’étudiant devra compléter plusieurs parties :
    - géométrie
    - forces
    - intégration temporelle
"""

# ============================================================
# IMPORTS
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# CONSTANTES PHYSIQUES
# ============================================================

rho_fluid = 1025      # masse volumique de l'eau de mer (kg/m^3)
g = 9.81              # gravité (m/s^2)

Cd = 0.5              # coefficient de traînée

# ============================================================
# GÉOMÉTRIE DE L'ANIMAL
# ============================================================

R = 0.10              # rayon externe (m)

# TODO :
# définir l'épaisseur e comme 10% du rayon

e = ...

# ============================================================
# ORIFICE D'ÉJECTION
# ============================================================

D_orifice = 0.02      # diamètre de l'orifice (m)

# TODO :
# calculer la section de l'orifice
# formule : A = pi * D^2 / 4

A_orifice = ...

# ============================================================
# VOLUMES
# ============================================================

# Volume externe de la sphère
# TODO :
# écrire la formule du volume d'une sphère

V_ext = ...

# Volume maximal interne
V_max = (4/3)*np.pi*(R - e)**3

# Volume minimal interne
V_min = 0.1 * V_max

# ============================================================
# MASSE DU CORPS
# ============================================================

rho_body = 1080

# Masse de la paroi
# TODO :
# compléter la formule

m_body = ...

# ============================================================
# MASSE AJOUTÉE
# ============================================================

# En mécanique des fluides :
# un objet accéléré doit aussi accélérer le fluide autour de lui

m_added_coeff = 0.5

# Surface de référence pour la traînée
S = np.pi * R**2

# ============================================================
# CYCLE DE CONTRACTION / EXPANSION
# ============================================================

T_contract = 0.5
T_expand = 2.0

T_cycle = T_contract + T_expand

# ============================================================
# FONCTION VOLUME(t)
# ============================================================

def volume(t):

    """
    Renvoie le volume interne de l'animal au temps t.
    """

    tau = t % T_cycle

    # Phase de contraction
    if tau < T_contract:

        return V_max - (V_max - V_min) * (tau / T_contract)

    # Phase d'expansion
    else:

        tau2 = tau - T_contract

        return V_min + (V_max - V_min) * (tau2 / T_expand)

# ============================================================
# dV/dt
# ============================================================

def dVdt(t):

    """
    Dérivée temporelle du volume.
    """

    tau = t % T_cycle

    # TODO :
    # compléter la dérivée pendant la contraction

    if tau < T_contract:

        return ...

    else:

        # TODO :
        # compléter la dérivée pendant l'expansion

        return ...

# ============================================================
# PARAMÈTRES NUMÉRIQUES
# ============================================================

dt = 0.001            # pas de temps (s)

T = 10                # temps total (s)

N = int(T/dt)

# ============================================================
# TABLEAUX DE STOCKAGE
# ============================================================

t = np.linspace(0, T, N)

z = np.zeros(N)       # position
v = np.zeros(N)       # vitesse
acc = np.zeros(N)     # accélération

vol = np.zeros(N)

# ============================================================
# BOUCLE TEMPORELLE
# ============================================================

for i in range(N-1):

    # ========================================================
    # Volume et variation de volume
    # ========================================================

    V = volume(t[i])

    dV = dVdt(t[i])

    # ========================================================
    # Masse du fluide contenu
    # ========================================================

    # TODO :
    # calculer la masse d'eau contenue dans l'animal

    m_fluid = ...

    # Masse totale
    m_total = m_body + m_fluid

    # ========================================================
    # Masse ajoutée
    # ========================================================

    # TODO :
    # compléter la formule de masse ajoutée

    m_added = ...

    # Masse effective
    m_eff = m_total + m_added

    # ========================================================
    # Débit
    # ========================================================

    # Débit volumique
    Q = dV

    # TODO :
    # calculer le débit massique

    mdot = ...

    # TODO :
    # calculer la vitesse d'éjection

    v_rel = ...

    # ========================================================
    # Force de propulsion
    # ========================================================

    # TODO :
    # compléter la poussée liée à l'éjection d'eau

    F_mass = ...

    # ========================================================
    # POIDS
    # ========================================================

    F_gravity = m_total * g

    # ========================================================
    # POUSSÉE D'ARCHIMÈDE
    # ========================================================

    # TODO :
    # compléter la poussée d'Archimède

    F_buoyancy = ...

    # ========================================================
    # TRAÎNÉE
    # ========================================================

    # TODO :
    # compléter la force de traînée quadratique

    F_drag = ...

    # ========================================================
    # SOMME DES FORCES
    # ========================================================

    F_ext = F_buoyancy - F_gravity - F_drag

    # ========================================================
    # ACCÉLÉRATION
    # ========================================================

    # TODO :
    # écrire la deuxième loi de Newton

    a = ...

    # ========================================================
    # SCHÉMA D'EULER
    # ========================================================

    # TODO :
    # mettre à jour la vitesse

    v[i+1] = ...

    # TODO :
    # mettre à jour la position

    z[i+1] = ...

    # stockage
    acc[i+1] = a
    vol[i+1] = V

# ============================================================
# GRAPHIQUES
# ============================================================

plt.figure()
plt.plot(t, z)
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.title("Position verticale")
plt.grid()

plt.figure()
plt.plot(t, v)
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse (m/s)")
plt.title("Vitesse")
plt.grid()

plt.figure()
plt.plot(t, acc)
plt.xlabel("Temps (s)")
plt.ylabel("Accélération (m/s²)")
plt.title("Accélération")
plt.grid()

plt.figure()
plt.plot(t, vol)
plt.xlabel("Temps (s)")
plt.ylabel("Volume (m³)")
plt.title("Volume interne")
plt.grid()

plt.show()