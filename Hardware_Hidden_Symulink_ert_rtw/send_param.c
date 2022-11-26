/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: send_param.c
 *
 * Code generated for Simulink model 'Hardware_Hidden_Symulink'.
 *
 * Model version                  : 1.52
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Sat Nov 26 13:10:12 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "Hardware_Hidden_Symulink_types.h"
#include "send_param_private.h"
#include "Hardware_Hidden_Symulink.h"
#include "send_param.h"
#include <string.h>
#include "rtwtypes.h"
#include <stddef.h>

/* Forward declaration for local functions */
static void Hardware_Hidde_SystemCore_setup(freedomk64f_SCIWrite_Hardware_T *obj);
static void Hardware_Hidde_SystemCore_setup(freedomk64f_SCIWrite_Hardware_T *obj)
{
  MW_SCI_Parity_Type ParityValue;
  MW_SCI_StopBits_Type StopBitsValue;
  uint32_T RxPinLoc;
  uint32_T SCIModuleLoc;
  obj->isSetupComplete = false;
  obj->isInitialized = 1;
  RxPinLoc = MW_UNDEFINED_VALUE;
  SCIModuleLoc = 0;
  obj->MW_SCIHANDLE = MW_SCI_Open(&SCIModuleLoc, false, RxPinLoc, 10U);
  MW_SCI_SetBaudrate(obj->MW_SCIHANDLE, 115200U);
  StopBitsValue = MW_SCI_STOPBITS_1;
  ParityValue = MW_SCI_PARITY_NONE;
  MW_SCI_SetFrameFormat(obj->MW_SCIHANDLE, 8, ParityValue, StopBitsValue);
  obj->isSetupComplete = true;
}

/* System initialize for Simulink Function: '<Root>/Function-Call Subsystem' */
void send_param_Init(void)
{
  MW_AnalogIn_TriggerSource_Type trigger_val;
  freedomk64f_AnalogInput_Hardw_T *obj;

  /* Start for MATLABSystem: '<S2>/Atrium egram' */
  Hardware_Hidden_Symulink_DW.obj_n.matlabCodegenIsDeleted = true;
  Hardware_Hidden_Symulink_DW.obj_n.isInitialized = 0;
  Hardware_Hidden_Symulink_DW.obj_n.SampleTime = -1.0;
  Hardware_Hidden_Symulink_DW.obj_n.matlabCodegenIsDeleted = false;
  Hardware_Hidden_Symulink_DW.obj_n.SampleTime =
    Hardware_Hidden_Symulink_P.Atriumegram_SampleTime;
  obj = &Hardware_Hidden_Symulink_DW.obj_n;
  Hardware_Hidden_Symulink_DW.obj_n.isSetupComplete = false;
  Hardware_Hidden_Symulink_DW.obj_n.isInitialized = 1;
  obj->MW_ANALOGIN_HANDLE = MW_AnalogInSingle_Open(16U);
  trigger_val = MW_ANALOGIN_SOFTWARE_TRIGGER;
  MW_AnalogIn_SetTriggerSource
    (Hardware_Hidden_Symulink_DW.obj_n.MW_ANALOGIN_HANDLE, trigger_val, 0U);
  Hardware_Hidden_Symulink_DW.obj_n.isSetupComplete = true;

  /* Start for MATLABSystem: '<S2>/Ventricle egram' */
  Hardware_Hidden_Symulink_DW.obj_j.matlabCodegenIsDeleted = true;
  Hardware_Hidden_Symulink_DW.obj_j.isInitialized = 0;
  Hardware_Hidden_Symulink_DW.obj_j.SampleTime = -1.0;
  Hardware_Hidden_Symulink_DW.obj_j.matlabCodegenIsDeleted = false;
  Hardware_Hidden_Symulink_DW.obj_j.SampleTime =
    Hardware_Hidden_Symulink_P.Ventricleegram_SampleTime;
  obj = &Hardware_Hidden_Symulink_DW.obj_j;
  Hardware_Hidden_Symulink_DW.obj_j.isSetupComplete = false;
  Hardware_Hidden_Symulink_DW.obj_j.isInitialized = 1;
  obj->MW_ANALOGIN_HANDLE = MW_AnalogInSingle_Open(17U);
  trigger_val = MW_ANALOGIN_SOFTWARE_TRIGGER;
  MW_AnalogIn_SetTriggerSource
    (Hardware_Hidden_Symulink_DW.obj_j.MW_ANALOGIN_HANDLE, trigger_val, 0U);
  Hardware_Hidden_Symulink_DW.obj_j.isSetupComplete = true;

  /* Start for MATLABSystem: '<S2>/Serial Transmit' */
  Hardware_Hidden_Symulink_DW.obj_b.isInitialized = 0;
  Hardware_Hidden_Symulink_DW.obj_b.matlabCodegenIsDeleted = false;
  Hardware_Hidde_SystemCore_setup(&Hardware_Hidden_Symulink_DW.obj_b);
}

/* Output and update for Simulink Function: '<Root>/Function-Call Subsystem' */
void send_param(void)
{
  uint8_T status;

  /* MATLABSystem: '<S2>/Atrium egram' */
  if (Hardware_Hidden_Symulink_DW.obj_n.SampleTime !=
      Hardware_Hidden_Symulink_P.Atriumegram_SampleTime) {
    Hardware_Hidden_Symulink_DW.obj_n.SampleTime =
      Hardware_Hidden_Symulink_P.Atriumegram_SampleTime;
  }

  MW_AnalogIn_Start(Hardware_Hidden_Symulink_DW.obj_n.MW_ANALOGIN_HANDLE);

  /* SignalConversion generated from: '<S2>/Serial Transmit' incorporates:
   *  MATLABSystem: '<S2>/Atrium egram'
   */
  MW_AnalogInSingle_ReadResult
    (Hardware_Hidden_Symulink_DW.obj_n.MW_ANALOGIN_HANDLE,
     &Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[9], 7);

  /* MATLABSystem: '<S2>/Ventricle egram' */
  if (Hardware_Hidden_Symulink_DW.obj_j.SampleTime !=
      Hardware_Hidden_Symulink_P.Ventricleegram_SampleTime) {
    Hardware_Hidden_Symulink_DW.obj_j.SampleTime =
      Hardware_Hidden_Symulink_P.Ventricleegram_SampleTime;
  }

  MW_AnalogIn_Start(Hardware_Hidden_Symulink_DW.obj_j.MW_ANALOGIN_HANDLE);

  /* SignalConversion generated from: '<S2>/Serial Transmit' incorporates:
   *  DataTypeConversion: '<S2>/Cast To Double'
   *  DataTypeConversion: '<S2>/Cast To Double1'
   *  DataTypeConversion: '<S2>/Cast To Double2'
   *  DataTypeConversion: '<S2>/Cast To Double3'
   *  DataTypeConversion: '<S2>/Cast To Double4'
   *  DataTypeConversion: '<S2>/Cast To Double5'
   *  DataTypeConversion: '<S2>/Cast To Double6'
   *  DataTypeConversion: '<S2>/Cast To Double7'
   *  DataTypeConversion: '<S2>/Cast To Double8'
   *  MATLABSystem: '<S2>/Ventricle egram'
   *  SignalConversion generated from: '<S2>/ATR_DUTY_CYCLE'
   *  SignalConversion generated from: '<S2>/ATR_PW'
   *  SignalConversion generated from: '<S2>/LOWER_RATE_LIMIT'
   *  SignalConversion generated from: '<S2>/Mode'
   *  SignalConversion generated from: '<S2>/PERIOD'
   *  SignalConversion generated from: '<S2>/RP'
   *  SignalConversion generated from: '<S2>/VENT_DUTY_CYCLE'
   *  SignalConversion generated from: '<S2>/VENT_PW'
   *  SignalConversion generated from: '<S2>/VRP'
   */
  MW_AnalogInSingle_ReadResult
    (Hardware_Hidden_Symulink_DW.obj_j.MW_ANALOGIN_HANDLE,
     &Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[10], 7);
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[0] =
    Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[1] =
    Hardware_Hidden_Symulink_B.ATR_PW;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[2] =
    Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[3] =
    Hardware_Hidden_Symulink_B.LRL;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[4] =
    Hardware_Hidden_Symulink_B.Period;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[5] =
    Hardware_Hidden_Symulink_B.Mode;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[6] =
    Hardware_Hidden_Symulink_B.ARP;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[7] =
    Hardware_Hidden_Symulink_B.VENT_PW;
  Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[8] =
    Hardware_Hidden_Symulink_B.VRP;

  /* MATLABSystem: '<S2>/Serial Transmit' */
  status = 1U;
  while (status != 0) {
    memcpy((void *)&Hardware_Hidden_Symulink_B.TxDataLocChar[0], (void *)
           &Hardware_Hidden_Symulink_B.TmpSignalConversionAtSerial[0], (uint32_T)
           ((size_t)88 * sizeof(uint8_T)));
    status = MW_SCI_Transmit(Hardware_Hidden_Symulink_DW.obj_b.MW_SCIHANDLE,
      &Hardware_Hidden_Symulink_B.TxDataLocChar[0], 88U);
  }

  /* End of MATLABSystem: '<S2>/Serial Transmit' */
}

/* Termination for Simulink Function: '<Root>/Function-Call Subsystem' */
void send_param_Term(void)
{
  /* Terminate for MATLABSystem: '<S2>/Atrium egram' */
  if (!Hardware_Hidden_Symulink_DW.obj_n.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_n.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_n.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_n.isSetupComplete) {
      MW_AnalogIn_Stop(Hardware_Hidden_Symulink_DW.obj_n.MW_ANALOGIN_HANDLE);
      MW_AnalogIn_Close(Hardware_Hidden_Symulink_DW.obj_n.MW_ANALOGIN_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Atrium egram' */

  /* Terminate for MATLABSystem: '<S2>/Ventricle egram' */
  if (!Hardware_Hidden_Symulink_DW.obj_j.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_j.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_j.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_j.isSetupComplete) {
      MW_AnalogIn_Stop(Hardware_Hidden_Symulink_DW.obj_j.MW_ANALOGIN_HANDLE);
      MW_AnalogIn_Close(Hardware_Hidden_Symulink_DW.obj_j.MW_ANALOGIN_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Ventricle egram' */

  /* Terminate for MATLABSystem: '<S2>/Serial Transmit' */
  if (!Hardware_Hidden_Symulink_DW.obj_b.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_b.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_b.isSetupComplete) {
      MW_SCI_Close(Hardware_Hidden_Symulink_DW.obj_b.MW_SCIHANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Serial Transmit' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
