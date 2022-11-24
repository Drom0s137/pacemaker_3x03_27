/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: pacemakerA1.c
 *
 * Code generated for Simulink model 'pacemakerA1'.
 *
 * Model version                  : 1.19
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Mon Oct 17 16:08:50 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "pacemakerA1.h"
#include "rtwtypes.h"
#include <math.h>
#include "pacemakerA1_types.h"

/* Named constants for Chart: '<Root>/STATE' */
#define pacemakerA1_IN_AVPacing        ((uint8_T)1U)
#define pacemakerA1_IN_AVPacing1       ((uint8_T)3U)
#define pacemakerA1_IN_CharingC22      ((uint8_T)2U)
#define pacemakerA1_IN_CharingC23      ((uint8_T)4U)
#define pacemakerA1_IN_CharingC23_d    ((uint8_T)5U)
#define pacemakerA1_IN_Discharge       ((uint8_T)6U)

/* Block signals (default storage) */
B_pacemakerA1_T pacemakerA1_B;

/* Block states (default storage) */
DW_pacemakerA1_T pacemakerA1_DW;

/* Real-time model */
static RT_MODEL_pacemakerA1_T pacemakerA1_M_;
RT_MODEL_pacemakerA1_T *const pacemakerA1_M = &pacemakerA1_M_;

/* Forward declaration for local functions */
static void pacemak_enter_atomic_CharingC22(void);

/* Function for Chart: '<Root>/STATE' */
static void pacemak_enter_atomic_CharingC22(void)
{
  /* Constant: '<Root>/Constant1' */
  pacemakerA1_B.PACE_REF_PWM = pacemakerA1_P.Constant1_Value;
  pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.HIGH;
  pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
  pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
  pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
  pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
  pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.LOW;
  pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
  pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.HIGH;
}

/* Model step function */
void pacemakerA1_step(void)
{
  /* Chart: '<Root>/STATE' incorporates:
   *  Constant: '<Root>/Constant'
   *  Constant: '<Root>/Constant1'
   *  Constant: '<Root>/Constant2'
   *  Constant: '<Root>/Constant3'
   *  Constant: '<Root>/Constant4'
   *  Constant: '<Root>/Constant5'
   *  Product: '<Root>/Divide'
   */
  if (pacemakerA1_DW.temporalCounter_i1 < MAX_uint32_T) {
    pacemakerA1_DW.temporalCounter_i1++;
  }

  if (pacemakerA1_DW.is_active_c3_pacemakerA1 == 0U) {
    pacemakerA1_DW.is_active_c3_pacemakerA1 = 1U;
    if (pacemakerA1_P.Constant3_Value == 1.0) {
      pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_CharingC22;
      pacemakerA1_DW.temporalCounter_i1 = 0U;
      pacemak_enter_atomic_CharingC22();
    } else if (pacemakerA1_P.Constant3_Value == 2.0) {
      pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_CharingC23_d;
      pacemakerA1_DW.temporalCounter_i1 = 0U;
    } else {
      pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_CharingC23;
      pacemakerA1_DW.temporalCounter_i1 = 0U;
      pacemak_enter_atomic_CharingC22();
    }
  } else {
    switch (pacemakerA1_DW.is_c3_pacemakerA1) {
     case pacemakerA1_IN_AVPacing:
      if (pacemakerA1_DW.temporalCounter_i1 >= (uint32_T)ceil
          (pacemakerA1_P.Constant_Value)) {
        pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_CharingC22;
        pacemakerA1_DW.temporalCounter_i1 = 0U;
        pacemak_enter_atomic_CharingC22();
      } else {
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
      }
      break;

     case pacemakerA1_IN_CharingC22:
      if (pacemakerA1_DW.temporalCounter_i1 >= (uint32_T)ceil
          (pacemakerA1_P.Constant2_Value / pacemakerA1_P.Constant4_Value -
           pacemakerA1_P.Constant_Value)) {
        pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_AVPacing;
        pacemakerA1_DW.temporalCounter_i1 = 0U;
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
      } else {
        pacemakerA1_B.PACE_REF_PWM = pacemakerA1_P.Constant1_Value;
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.HIGH;
      }
      break;

     case pacemakerA1_IN_AVPacing1:
      if (pacemakerA1_DW.temporalCounter_i1 >= (uint32_T)ceil
          (pacemakerA1_P.Constant_Value)) {
        pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_CharingC23;
        pacemakerA1_DW.temporalCounter_i1 = 0U;
        pacemak_enter_atomic_CharingC22();
      } else {
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
      }
      break;

     case pacemakerA1_IN_CharingC23:
      if (pacemakerA1_DW.temporalCounter_i1 >= (uint32_T)ceil
          (pacemakerA1_P.Constant2_Value / pacemakerA1_P.Constant4_Value -
           pacemakerA1_P.Constant_Value)) {
        pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_AVPacing1;
        pacemakerA1_DW.temporalCounter_i1 = 0U;
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
      } else {
        pacemakerA1_B.PACE_REF_PWM = pacemakerA1_P.Constant1_Value;
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.HIGH;
      }
      break;

     case pacemakerA1_IN_CharingC23_d:
      if (pacemakerA1_DW.temporalCounter_i1 >= (uint32_T)ceil
          (pacemakerA1_P.Constant2_Value / pacemakerA1_P.Constant4_Value -
           pacemakerA1_P.Constant5_Value)) {
        pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_Discharge;
        pacemakerA1_DW.temporalCounter_i1 = 0U;
      } else {
        pacemakerA1_B.PACE_REF_PWM = pacemakerA1_P.Constant1_Value;
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.HIGH;
      }
      break;

     default:
      /* case IN_Discharge: */
      if (pacemakerA1_DW.temporalCounter_i1 >= (uint32_T)ceil
          (pacemakerA1_P.Constant5_Value)) {
        pacemakerA1_DW.is_c3_pacemakerA1 = pacemakerA1_IN_CharingC23_d;
        pacemakerA1_DW.temporalCounter_i1 = 0U;
      } else {
        pacemakerA1_B.PACE_CHARGE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.PACE_GND_CTRL = pacemakerA1_DW.HIGH;
        pacemakerA1_B.ATR_PACE_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.ATR_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_ATR_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.Z_VENT_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_GND_CTRL = pacemakerA1_DW.LOW;
        pacemakerA1_B.VENT_PACE_CTRL = pacemakerA1_DW.HIGH;
      }
      break;
    }
  }

  /* End of Chart: '<Root>/STATE' */

  /* MATLABSystem: '<S2>/Digital Write' */
  MW_digitalIO_write(pacemakerA1_DW.obj_h.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.ATR_GND_CTRL);

  /* MATLABSystem: '<S2>/Digital Write1' */
  MW_digitalIO_write(pacemakerA1_DW.obj_j.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.PACE_CHARGE_CTRL);

  /* MATLABSystem: '<S2>/Digital Write2' */
  MW_digitalIO_write(pacemakerA1_DW.obj_l.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.ATR_PACE_CTRL);

  /* MATLABSystem: '<S2>/Digital Write3' */
  MW_digitalIO_write(pacemakerA1_DW.obj_e.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.PACE_GND_CTRL);

  /* MATLABSystem: '<S2>/Digital Write4' */
  MW_digitalIO_write(pacemakerA1_DW.obj_f.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.VENT_GND_CTRL);

  /* MATLABSystem: '<S2>/Digital Write5' */
  MW_digitalIO_write(pacemakerA1_DW.obj_m.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.VENT_PACE_CTRL);

  /* MATLABSystem: '<S2>/Digital Write6' */
  MW_digitalIO_write(pacemakerA1_DW.obj_p.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.Z_VENT_CTRL);

  /* MATLABSystem: '<S2>/Digital Write7' */
  MW_digitalIO_write(pacemakerA1_DW.obj_k.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.Z_ATR_CTRL);

  /* MATLABSystem: '<S2>/Digital Write8' */
  MW_digitalIO_write(pacemakerA1_DW.obj.MW_DIGITALIO_HANDLE,
                     pacemakerA1_B.PACE_REF_PWM != 0.0);
}

/* Model initialize function */
void pacemakerA1_initialize(void)
{
  {
    freedomk64f_DigitalWrite_pace_T *obj;

    /* SystemInitialize for Chart: '<Root>/STATE' */
    pacemakerA1_DW.HIGH = true;

    /* Start for MATLABSystem: '<S2>/Digital Write' */
    pacemakerA1_DW.obj_h.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_h.isInitialized = 0;
    pacemakerA1_DW.obj_h.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_h;
    pacemakerA1_DW.obj_h.isSetupComplete = false;
    pacemakerA1_DW.obj_h.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    pacemakerA1_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write1' */
    pacemakerA1_DW.obj_j.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_j.isInitialized = 0;
    pacemakerA1_DW.obj_j.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_j;
    pacemakerA1_DW.obj_j.isSetupComplete = false;
    pacemakerA1_DW.obj_j.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    pacemakerA1_DW.obj_j.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write2' */
    pacemakerA1_DW.obj_l.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_l.isInitialized = 0;
    pacemakerA1_DW.obj_l.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_l;
    pacemakerA1_DW.obj_l.isSetupComplete = false;
    pacemakerA1_DW.obj_l.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    pacemakerA1_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write3' */
    pacemakerA1_DW.obj_e.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_e.isInitialized = 0;
    pacemakerA1_DW.obj_e.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_e;
    pacemakerA1_DW.obj_e.isSetupComplete = false;
    pacemakerA1_DW.obj_e.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    pacemakerA1_DW.obj_e.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write4' */
    pacemakerA1_DW.obj_f.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_f.isInitialized = 0;
    pacemakerA1_DW.obj_f.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_f;
    pacemakerA1_DW.obj_f.isSetupComplete = false;
    pacemakerA1_DW.obj_f.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    pacemakerA1_DW.obj_f.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write5' */
    pacemakerA1_DW.obj_m.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_m.isInitialized = 0;
    pacemakerA1_DW.obj_m.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_m;
    pacemakerA1_DW.obj_m.isSetupComplete = false;
    pacemakerA1_DW.obj_m.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    pacemakerA1_DW.obj_m.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write6' */
    pacemakerA1_DW.obj_p.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_p.isInitialized = 0;
    pacemakerA1_DW.obj_p.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_p;
    pacemakerA1_DW.obj_p.isSetupComplete = false;
    pacemakerA1_DW.obj_p.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    pacemakerA1_DW.obj_p.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write7' */
    pacemakerA1_DW.obj_k.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj_k.isInitialized = 0;
    pacemakerA1_DW.obj_k.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj_k;
    pacemakerA1_DW.obj_k.isSetupComplete = false;
    pacemakerA1_DW.obj_k.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    pacemakerA1_DW.obj_k.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write8' */
    pacemakerA1_DW.obj.matlabCodegenIsDeleted = true;
    pacemakerA1_DW.obj.isInitialized = 0;
    pacemakerA1_DW.obj.matlabCodegenIsDeleted = false;
    obj = &pacemakerA1_DW.obj;
    pacemakerA1_DW.obj.isSetupComplete = false;
    pacemakerA1_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(5U, 1);
    pacemakerA1_DW.obj.isSetupComplete = true;
  }
}

/* Model terminate function */
void pacemakerA1_terminate(void)
{
  /* Terminate for MATLABSystem: '<S2>/Digital Write' */
  if (!pacemakerA1_DW.obj_h.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_h.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_h.isInitialized == 1) &&
        pacemakerA1_DW.obj_h.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_h.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write1' */
  if (!pacemakerA1_DW.obj_j.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_j.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_j.isInitialized == 1) &&
        pacemakerA1_DW.obj_j.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_j.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write1' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write2' */
  if (!pacemakerA1_DW.obj_l.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_l.isInitialized == 1) &&
        pacemakerA1_DW.obj_l.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_l.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write2' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write3' */
  if (!pacemakerA1_DW.obj_e.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_e.isInitialized == 1) &&
        pacemakerA1_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write3' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write4' */
  if (!pacemakerA1_DW.obj_f.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_f.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_f.isInitialized == 1) &&
        pacemakerA1_DW.obj_f.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_f.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write4' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write5' */
  if (!pacemakerA1_DW.obj_m.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_m.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_m.isInitialized == 1) &&
        pacemakerA1_DW.obj_m.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_m.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write5' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write6' */
  if (!pacemakerA1_DW.obj_p.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_p.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_p.isInitialized == 1) &&
        pacemakerA1_DW.obj_p.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_p.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write6' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write7' */
  if (!pacemakerA1_DW.obj_k.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj_k.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj_k.isInitialized == 1) &&
        pacemakerA1_DW.obj_k.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj_k.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write7' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write8' */
  if (!pacemakerA1_DW.obj.matlabCodegenIsDeleted) {
    pacemakerA1_DW.obj.matlabCodegenIsDeleted = true;
    if ((pacemakerA1_DW.obj.isInitialized == 1) &&
        pacemakerA1_DW.obj.isSetupComplete) {
      MW_digitalIO_close(pacemakerA1_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write8' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
