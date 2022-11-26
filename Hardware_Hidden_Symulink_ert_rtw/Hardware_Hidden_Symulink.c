/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Hardware_Hidden_Symulink.c
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

#include "Hardware_Hidden_Symulink.h"
#include "rtwtypes.h"
#include "Hardware_Hidden_Symulink_types.h"
#include <string.h>
#include "rt_roundd_snf.h"
#include <math.h>
#include <stddef.h>
#include "rt_nonfinite.h"
#include "send_param.h"
#include "send_param_private.h"

/* Named constants for Chart: '<Root>/ states  ' */
#define Hardware_Hi_IN_CharingC23_nnrds ((uint8_T)17U)
#define Hardware_Hid_IN_CharingC23_nnrd ((uint8_T)16U)
#define Hardware_Hidd_IN_CharingC23_nnr ((uint8_T)13U)
#define Hardware_Hidde_IN_CharingC23_nn ((uint8_T)11U)
#define Hardware_Hidde_IN_DISCHARGING_f ((uint8_T)21U)
#define Hardware_Hidden_IN_CharingC22_c ((uint8_T)8U)
#define Hardware_Hidden_IN_CharingC23_n ((uint8_T)10U)
#define Hardware_Hidden_IN_Discharge_oe ((uint8_T)18U)
#define Hardware_Hidden_S_IN_AVPacing_k ((uint8_T)7U)
#define Hardware_Hidden_S_IN_CharingC22 ((uint8_T)2U)
#define Hardware_Hidden_S_IN_CharingC23 ((uint8_T)4U)
#define Hardware_Hidden_Sy_IN_AVPacing1 ((uint8_T)9U)
#define Hardware_Hidden_Sy_IN_Discharge ((uint8_T)12U)
#define Hardware_Hidden_Sy_IN_Inhibit_o ((uint8_T)19U)
#define Hardware_Hidden_Sym_IN_AVPacing ((uint8_T)1U)
#define Hardware_Hidden_Sym_IN_CHARGING ((uint8_T)20U)
#define Hardware_Hidden_Symu_IN_Inhibit ((uint8_T)3U)
#define Hardware_Hidden_Symuli_IN_PROXY ((uint8_T)22U)
#define Hardware_Hidden_Symuli_IN_Proxy ((uint8_T)6U)
#define Hardware_Hidden__IN_AVPacing1_b ((uint8_T)15U)
#define Hardware_Hidden__IN_DISCHARGING ((uint8_T)5U)
#define Hardware_Hidden__IN_Discharge_o ((uint8_T)14U)

/* Named constants for Chart: '<S4>/Chart' */
#define Hardware_Hidden_S_IN_Echo_Param ((uint8_T)1U)
#define Hardware_Hidden_Sy_IN_Set_Param ((uint8_T)3U)
#define Hardware_Hidden_Symu_IN_Initial ((uint8_T)2U)
#define Hardware_Hidden_Symu_IN_StandBy ((uint8_T)4U)

/* Named constants for Chart: '<S5>/Chart' */
#define Hardware_Hidden_Symu_IN_S2FAIL1 ((uint8_T)1U)
#define Hardware_Hidden_Symul_IN_Start1 ((uint8_T)5U)
#define Hardware_Hidden_Symulink_IN_S3 ((uint8_T)2U)
#define Hardware_Hidden_Symulink_IN_S4 ((uint8_T)3U)
#define Hardware_Hidden__IN_S_FAILSAFE1 ((uint8_T)4U)

/* Block signals (default storage) */
B_Hardware_Hidden_Symulink_T Hardware_Hidden_Symulink_B;

/* Block states (default storage) */
DW_Hardware_Hidden_Symulink_T Hardware_Hidden_Symulink_DW;

/* Real-time model */
static RT_MODEL_Hardware_Hidden_Symu_T Hardware_Hidden_Symulink_M_;
RT_MODEL_Hardware_Hidden_Symu_T *const Hardware_Hidden_Symulink_M =
  &Hardware_Hidden_Symulink_M_;

/* Forward declaration for local functions */
static int16_T Hardware_Hidd_bitshift_anonFcn1(int16_T a1, real_T k1);
static void Hardware_Hidden_Symu_CharingC22(const boolean_T *ATR_DETECT);
static void Hardware_Hidden_Sy_CharingC22_p(void);
static void Hardware_Hidden_Symu_CharingC23(const boolean_T *VENT_DETECT);
static void enter_internal_c3_Hardware_Hidd(void);
static void Hardware_Hi_SystemCore_setup_hp(freedomk64f_SCIRead_Hardware__T *obj);
static void Hardware_Hid_SystemCore_setup_h(freedomk64f_fxos8700_Hardware_T *obj);
static void rate_monotonic_scheduler(void);

/*
 * Set which subrates need to run this base step (base rate always runs).
 * This function must be called prior to calling the model step function
 * in order to remember which rates need to run this base step.  The
 * buffering of events allows for overlapping preemption.
 */
void Hardware_Hidden_Symulink_SetEventsForThisBaseStep(boolean_T *eventFlags)
{
  /* Task runs when its counter is zero, computed via rtmStepTask macro */
  eventFlags[1] = ((boolean_T)rtmStepTask(Hardware_Hidden_Symulink_M, 1));
}

/*
 *         This function updates active task flag for each subrate
 *         and rate transition flags for tasks that exchange data.
 *         The function assumes rate-monotonic multitasking scheduler.
 *         The function must be called at model base rate so that
 *         the generated code self-manages all its subrates and rate
 *         transition flags.
 */
static void rate_monotonic_scheduler(void)
{
  /* Compute which subrates run during the next base time step.  Subrates
   * are an integer multiple of the base rate counter.  Therefore, the subtask
   * counter is reset when it reaches its limit (zero means run).
   */
  (Hardware_Hidden_Symulink_M->Timing.TaskCounters.TID[1])++;
  if ((Hardware_Hidden_Symulink_M->Timing.TaskCounters.TID[1]) > 99) {/* Sample time: [0.1s, 0.0s] */
    Hardware_Hidden_Symulink_M->Timing.TaskCounters.TID[1] = 0;
  }
}

static int16_T Hardware_Hidd_bitshift_anonFcn1(int16_T a1, real_T k1)
{
  int16_T varargout_1;
  if (k1 >= 0.0) {
    if (k1 <= 15.0) {
      varargout_1 = (int16_T)(a1 << (uint8_T)k1);
    } else {
      varargout_1 = 0;
    }
  } else if (k1 >= -15.0) {
    varargout_1 = (int16_T)(a1 >> (uint8_T)-k1);
  } else if (a1 < 0) {
    varargout_1 = -1;
  } else {
    varargout_1 = 0;
  }

  return varargout_1;
}

/* Function for Chart: '<Root>/ states  ' */
static void Hardware_Hidden_Symu_CharingC22(const boolean_T *ATR_DETECT)
{
  uint32_T qY;
  if (((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 * 100)
       >= Hardware_Hidden_Symulink_B.LRL) && (*ATR_DETECT ==
       Hardware_Hidden_Symulink_DW.HIGH)) {
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_Symu_IN_Inhibit;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    Hardware_Hidden_Symulink_B.PACE_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.ATR_PACE_CTRL = Hardware_Hidden_Symulink_DW.LOW;
    Hardware_Hidden_Symulink_B.ATR_GND_CTRL = Hardware_Hidden_Symulink_DW.LOW;
  } else {
    qY = (uint32_T)Hardware_Hidden_Symulink_B.Period - /*MW:OvSatOk*/
      Hardware_Hidden_Symulink_B.ATR_PW;
    if (qY > Hardware_Hidden_Symulink_B.Period) {
      qY = 0U;
    }

    if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 * 100)
        >= qY) {
      Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
        Hardware_Hidden_Sym_IN_AVPacing;
      Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
        Hardware_Hidden_Symulink_DW.LOW;
      Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
        Hardware_Hidden_Symulink_DW.HIGH;
      Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
        Hardware_Hidden_Symulink_DW.HIGH;
      Hardware_Hidden_Symulink_B.ATR_GND_CTRL = Hardware_Hidden_Symulink_DW.LOW;
    } else {
      Hardware_Hidden_Symulink_B.PACE_REF_PWM =
        Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
      Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
        Hardware_Hidden_Symulink_DW.HIGH;
      Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
        Hardware_Hidden_Symulink_DW.HIGH;
      Hardware_Hidden_Symulink_B.ATR_PACE_CTRL = Hardware_Hidden_Symulink_DW.LOW;
      Hardware_Hidden_Symulink_B.ATR_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    }
  }
}

/* Function for Chart: '<Root>/ states  ' */
static void Hardware_Hidden_Sy_CharingC22_p(void)
{
  uint32_T qY;
  qY = (uint32_T)Hardware_Hidden_Symulink_B.Period - /*MW:OvSatOk*/
    Hardware_Hidden_Symulink_B.ATR_PW;
  if (qY > Hardware_Hidden_Symulink_B.Period) {
    qY = 0U;
  }

  if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 * 100) >=
      qY) {
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_S_IN_AVPacing_k;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
      Hardware_Hidden_Symulink_DW.LOW;
    Hardware_Hidden_Symulink_B.PACE_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.ATR_PACE_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.ATR_GND_CTRL = Hardware_Hidden_Symulink_DW.LOW;
  } else {
    Hardware_Hidden_Symulink_B.PACE_REF_PWM =
      Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
    Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
      Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.PACE_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.ATR_PACE_CTRL = Hardware_Hidden_Symulink_DW.LOW;
    Hardware_Hidden_Symulink_B.ATR_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
  }
}

/* Function for Chart: '<Root>/ states  ' */
static void Hardware_Hidden_Symu_CharingC23(const boolean_T *VENT_DETECT)
{
  uint32_T qY;
  uint32_T tmp;
  qY = (uint32_T)Hardware_Hidden_Symulink_B.Period - /*MW:OvSatOk*/
    Hardware_Hidden_Symulink_B.VENT_PW;
  if (qY > Hardware_Hidden_Symulink_B.Period) {
    qY = 0U;
  }

  tmp = (uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 * 100);
  if ((tmp >= qY) && (*VENT_DETECT == Hardware_Hidden_Symulink_DW.LOW)) {
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_IN_Discharge_oe;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
  } else if ((tmp >= Hardware_Hidden_Symulink_B.LRL) && (*VENT_DETECT ==
              Hardware_Hidden_Symulink_DW.HIGH)) {
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_Sy_IN_Inhibit_o;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    Hardware_Hidden_Symulink_B.PACE_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.VENT_PACE_CTRL = Hardware_Hidden_Symulink_DW.LOW;
    Hardware_Hidden_Symulink_B.VENT_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
  } else {
    Hardware_Hidden_Symulink_B.PACE_REF_PWM =
      Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE;
    Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
      Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.PACE_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.VENT_PACE_CTRL = Hardware_Hidden_Symulink_DW.LOW;
    Hardware_Hidden_Symulink_B.VENT_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
  }
}

/* Function for Chart: '<Root>/ states  ' */
static void enter_internal_c3_Hardware_Hidd(void)
{
  switch (Hardware_Hidden_Symulink_B.Mode) {
   case 1:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_IN_CharingC22_c;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    Hardware_Hidden_Symulink_B.PACE_REF_PWM =
      Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
    Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
      Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.PACE_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.ATR_PACE_CTRL = Hardware_Hidden_Symulink_DW.LOW;
    Hardware_Hidden_Symulink_B.ATR_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    break;

   case 2:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidd_IN_CharingC23_nnr;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    break;

   case 3:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hi_IN_CharingC23_nnrds;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    break;

   case 4:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_S_IN_CharingC22;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    Hardware_Hidden_Symulink_B.PACE_REF_PWM =
      Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
    Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
      Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.PACE_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    Hardware_Hidden_Symulink_B.ATR_PACE_CTRL = Hardware_Hidden_Symulink_DW.LOW;
    Hardware_Hidden_Symulink_B.ATR_GND_CTRL = Hardware_Hidden_Symulink_DW.HIGH;
    break;

   case 5:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_IN_CharingC23_n;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    break;

   case 6:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hid_IN_CharingC23_nnrd;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    break;

   case 7:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_S_IN_CharingC23;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    break;

   case 8:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidden_Sym_IN_CHARGING;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    break;

   default:
    Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
      Hardware_Hidde_IN_CharingC23_nn;
    Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
    break;
  }
}

static void Hardware_Hi_SystemCore_setup_hp(freedomk64f_SCIRead_Hardware__T *obj)
{
  obj->isSetupComplete = false;
  obj->isInitialized = 1;
  Hardware_Hidden_Symulink_B.TxPinLoc = MW_UNDEFINED_VALUE;
  Hardware_Hidden_Symulink_B.SCIModuleLoc = 0;
  obj->MW_SCIHANDLE = MW_SCI_Open(&Hardware_Hidden_Symulink_B.SCIModuleLoc,
    false, 10U, Hardware_Hidden_Symulink_B.TxPinLoc);
  MW_SCI_SetBaudrate(obj->MW_SCIHANDLE, 115200U);
  Hardware_Hidden_Symulink_B.StopBitsValue = MW_SCI_STOPBITS_1;
  Hardware_Hidden_Symulink_B.ParityValue = MW_SCI_PARITY_NONE;
  MW_SCI_SetFrameFormat(obj->MW_SCIHANDLE, 8,
                        Hardware_Hidden_Symulink_B.ParityValue,
                        Hardware_Hidden_Symulink_B.StopBitsValue);
  obj->isSetupComplete = true;
}

static void Hardware_Hid_SystemCore_setup_h(freedomk64f_fxos8700_Hardware_T *obj)
{
  obj->isSetupComplete = false;
  obj->isInitialized = 1;
  Hardware_Hidden_Symulink_B.ModeType = MW_I2C_MASTER;
  Hardware_Hidden_Symulink_B.i2cname = 0;
  obj->i2cobj.MW_I2C_HANDLE = MW_I2C_Open(Hardware_Hidden_Symulink_B.i2cname,
    Hardware_Hidden_Symulink_B.ModeType);
  obj->i2cobj.BusSpeed = 100000U;
  MW_I2C_SetBusSpeed(obj->i2cobj.MW_I2C_HANDLE, obj->i2cobj.BusSpeed);
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0] = 43U;
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[1] = 64U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     &Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0], 2U,
                     false, false);
  OSA_TimeDelay(500U);
  Hardware_Hidden_Symulink_B.status = 42U;
  Hardware_Hidden_Symulink_B.status = MW_I2C_MasterWrite
    (obj->i2cobj.MW_I2C_HANDLE, 29U, &Hardware_Hidden_Symulink_B.status, 1U,
     true, false);
  if (Hardware_Hidden_Symulink_B.status == 0) {
    MW_I2C_MasterRead(obj->i2cobj.MW_I2C_HANDLE, 29U,
                      &Hardware_Hidden_Symulink_B.status, 1U, false, true);
    memcpy((void *)&Hardware_Hidden_Symulink_B.b_RegisterValue, (void *)
           &Hardware_Hidden_Symulink_B.status, (uint32_T)((size_t)1 * sizeof
            (uint8_T)));
  } else {
    Hardware_Hidden_Symulink_B.b_RegisterValue = 0U;
  }

  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0] = 42U;
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[1] = (uint8_T)
    (Hardware_Hidden_Symulink_B.b_RegisterValue & 254);
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     &Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0], 2U,
                     false, false);
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0] = 14U;
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[1] = 1U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     &Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0], 2U,
                     false, false);
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0] = 91U;
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[1] = 0U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     &Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0], 2U,
                     false, false);
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0] = 42U;
  Hardware_Hidden_Symulink_B.b_SwappedDataBytes[1] = 1U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U,
                     &Hardware_Hidden_Symulink_B.b_SwappedDataBytes[0], 2U,
                     false, false);
  obj->isSetupComplete = true;
}

/* Model step function for TID0 */
void Hardware_Hidden_Symulink_step0(void) /* Sample time: [0.001s, 0.0s] */
{
  {                                    /* Sample time: [0.001s, 0.0s] */
    rate_monotonic_scheduler();
  }
}

/* Model step function for TID1 */
void Hardware_Hidden_Symulink_step1(void) /* Sample time: [0.1s, 0.0s] */
{
  real_T rtb_FXOS87006AxesSensor_idx_0;
  real_T rtb_FXOS87006AxesSensor_idx_1;
  real_T rtb_FXOS87006AxesSensor_idx_2;
  int32_T rtb_Sum;
  uint32_T qY;
  int16_T b_RegisterValue[3];
  uint8_T output_raw[6];
  uint8_T b_x[2];
  uint8_T y[2];
  uint8_T status;
  boolean_T rtb_Compare;
  boolean_T tmp;
  boolean_T tmp_0;

  /* MATLABSystem: '<S4>/Serial Receive' */
  if (Hardware_Hidden_Symulink_DW.obj_m.SampleTime !=
      Hardware_Hidden_Symulink_P.SerialReceive_SampleTime) {
    Hardware_Hidden_Symulink_DW.obj_m.SampleTime =
      Hardware_Hidden_Symulink_P.SerialReceive_SampleTime;
  }

  status = MW_SCI_Receive(Hardware_Hidden_Symulink_DW.obj_m.MW_SCIHANDLE,
    &Hardware_Hidden_Symulink_B.RxDataLocChar[0], 19U);
  memcpy((void *)&Hardware_Hidden_Symulink_B.RxData[0], (void *)
         &Hardware_Hidden_Symulink_B.RxDataLocChar[0], (uint32_T)((size_t)19 *
          sizeof(uint8_T)));

  /* Chart: '<S4>/Chart' incorporates:
   *  MATLABSystem: '<S4>/Serial Receive'
   */
  if (Hardware_Hidden_Symulink_DW.is_active_c1_Hardware_Hidden_Sy == 0U) {
    Hardware_Hidden_Symulink_DW.is_active_c1_Hardware_Hidden_Sy = 1U;
    Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
      Hardware_Hidden_Symu_IN_Initial;
    Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE = 1U;
    Hardware_Hidden_Symulink_B.ATR_PW = 1U;
    Hardware_Hidden_Symulink_B.Mode = 1U;
    Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE = 1U;
    Hardware_Hidden_Symulink_B.VENT_PW = 1U;
    Hardware_Hidden_Symulink_B.ARP = 1U;
    Hardware_Hidden_Symulink_B.VRP = 1U;
    Hardware_Hidden_Symulink_B.LRL = 1U;
    Hardware_Hidden_Symulink_B.Period = MAX_uint8_T;
    Hardware_Hidden_Symulink_B.Activity_Threshold = 1U;
    Hardware_Hidden_Symulink_B.Response_Factor = 1U;
    Hardware_Hidden_Symulink_B.Recovery_Time = 1U;
    Hardware_Hidden_Symulink_B.Max_Sensor_Rate = 1U;
  } else {
    switch (Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink) {
     case Hardware_Hidden_S_IN_Echo_Param:
      Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
        Hardware_Hidden_Symu_IN_StandBy;
      break;

     case Hardware_Hidden_Symu_IN_Initial:
      Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
        Hardware_Hidden_Symu_IN_StandBy;
      break;

     case Hardware_Hidden_Sy_IN_Set_Param:
      Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
        Hardware_Hidden_Symu_IN_StandBy;
      break;

     default:
      /* case IN_StandBy: */
      if (status == 0) {
        if (Hardware_Hidden_Symulink_B.RxData[0] == 22) {
          switch (Hardware_Hidden_Symulink_B.RxData[1]) {
           case 85:
            Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
              Hardware_Hidden_Sy_IN_Set_Param;
            Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE =
              Hardware_Hidden_Symulink_B.RxData[2];
            Hardware_Hidden_Symulink_B.ATR_PW =
              Hardware_Hidden_Symulink_B.RxData[3];
            Hardware_Hidden_Symulink_B.Mode = Hardware_Hidden_Symulink_B.RxData
              [4];
            Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE =
              Hardware_Hidden_Symulink_B.RxData[5];
            Hardware_Hidden_Symulink_B.VENT_PW =
              Hardware_Hidden_Symulink_B.RxData[6];
            Hardware_Hidden_Symulink_B.ARP = Hardware_Hidden_Symulink_B.RxData[7];
            Hardware_Hidden_Symulink_B.VRP = Hardware_Hidden_Symulink_B.RxData[8];
            Hardware_Hidden_Symulink_B.LRL = Hardware_Hidden_Symulink_B.RxData[9];
            rtb_FXOS87006AxesSensor_idx_0 = rt_roundd_snf(60000.0 / (real_T)
              Hardware_Hidden_Symulink_B.LRL);
            if (rtb_FXOS87006AxesSensor_idx_0 < 256.0) {
              Hardware_Hidden_Symulink_B.Period = (uint8_T)
                rtb_FXOS87006AxesSensor_idx_0;
            } else {
              Hardware_Hidden_Symulink_B.Period = MAX_uint8_T;
            }

            Hardware_Hidden_Symulink_B.Activity_Threshold =
              Hardware_Hidden_Symulink_B.RxData[10];
            Hardware_Hidden_Symulink_B.Response_Factor =
              Hardware_Hidden_Symulink_B.RxData[11];
            Hardware_Hidden_Symulink_B.Recovery_Time =
              Hardware_Hidden_Symulink_B.RxData[12];
            Hardware_Hidden_Symulink_B.Max_Sensor_Rate =
              Hardware_Hidden_Symulink_B.RxData[13];
            break;

           case 34:
            Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
              Hardware_Hidden_S_IN_Echo_Param;
            send_param();
            break;

           default:
            Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
              Hardware_Hidden_Symu_IN_StandBy;
            break;
          }
        } else {
          Hardware_Hidden_Symulink_DW.is_c1_Hardware_Hidden_Symulink =
            Hardware_Hidden_Symu_IN_StandBy;
        }
      }
      break;
    }
  }

  /* End of Chart: '<S4>/Chart' */

  /* MATLABSystem: '<S3>/ATR_DETECT' */
  if (Hardware_Hidden_Symulink_DW.obj_g.SampleTime !=
      Hardware_Hidden_Symulink_P.ATR_DETECT_SampleTime) {
    Hardware_Hidden_Symulink_DW.obj_g.SampleTime =
      Hardware_Hidden_Symulink_P.ATR_DETECT_SampleTime;
  }

  tmp = MW_digitalIO_read(Hardware_Hidden_Symulink_DW.obj_g.MW_DIGITALIO_HANDLE);

  /* MATLABSystem: '<S3>/VENT_DETECT' */
  if (Hardware_Hidden_Symulink_DW.obj_n2.SampleTime !=
      Hardware_Hidden_Symulink_P.VENT_DETECT_SampleTime) {
    Hardware_Hidden_Symulink_DW.obj_n2.SampleTime =
      Hardware_Hidden_Symulink_P.VENT_DETECT_SampleTime;
  }

  tmp_0 = MW_digitalIO_read
    (Hardware_Hidden_Symulink_DW.obj_n2.MW_DIGITALIO_HANDLE);

  /* MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor' */
  if (Hardware_Hidden_Symulink_DW.obj.SampleTime !=
      Hardware_Hidden_Symulink_P.FXOS87006AxesSensor_SampleTime) {
    Hardware_Hidden_Symulink_DW.obj.SampleTime =
      Hardware_Hidden_Symulink_P.FXOS87006AxesSensor_SampleTime;
  }

  status = 1U;
  status = MW_I2C_MasterWrite
    (Hardware_Hidden_Symulink_DW.obj.i2cobj.MW_I2C_HANDLE, 29U, &status, 1U,
     true, false);
  if (status == 0) {
    MW_I2C_MasterRead(Hardware_Hidden_Symulink_DW.obj.i2cobj.MW_I2C_HANDLE, 29U,
                      &output_raw[0], 6U, false, true);
    memcpy((void *)&b_RegisterValue[0], (void *)&output_raw[0], (uint32_T)
           ((size_t)3 * sizeof(int16_T)));
    memcpy((void *)&y[0], (void *)&b_RegisterValue[0], (uint32_T)((size_t)2 *
            sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&b_RegisterValue[0], (void *)&b_x[0], (uint32_T)((size_t)1 *
            sizeof(int16_T)));
    memcpy((void *)&y[0], (void *)&b_RegisterValue[1], (uint32_T)((size_t)2 *
            sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&b_RegisterValue[1], (void *)&b_x[0], (uint32_T)((size_t)1 *
            sizeof(int16_T)));
    memcpy((void *)&y[0], (void *)&b_RegisterValue[2], (uint32_T)((size_t)2 *
            sizeof(uint8_T)));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&b_RegisterValue[2], (void *)&b_x[0], (uint32_T)((size_t)1 *
            sizeof(int16_T)));
  } else {
    b_RegisterValue[0] = 0;
    b_RegisterValue[1] = 0;
    b_RegisterValue[2] = 0;
  }

  rtb_FXOS87006AxesSensor_idx_0 = (real_T)Hardware_Hidd_bitshift_anonFcn1
    (b_RegisterValue[0], -2.0) * 2.0 * 0.244 / 1000.0;
  rtb_FXOS87006AxesSensor_idx_1 = (real_T)Hardware_Hidd_bitshift_anonFcn1
    (b_RegisterValue[1], -2.0) * 2.0 * 0.244 / 1000.0;
  rtb_FXOS87006AxesSensor_idx_2 = (real_T)Hardware_Hidd_bitshift_anonFcn1
    (b_RegisterValue[2], -2.0) * 2.0 * 0.244 / 1000.0;

  /* End of MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor' */

  /* RelationalOperator: '<S10>/Compare' incorporates:
   *  Constant: '<S10>/Constant'
   *  DotProduct: '<S5>/Dot Product'
   *  DotProduct: '<S5>/Dot Product1'
   *  DotProduct: '<S5>/Dot Product2'
   *  Sqrt: '<S5>/Sqrt'
   *  Sum: '<S5>/Add'
   *  Sum: '<S5>/Subtract'
   */
  rtb_Compare = (sqrt((rtb_FXOS87006AxesSensor_idx_0 *
                       rtb_FXOS87006AxesSensor_idx_0 +
                       rtb_FXOS87006AxesSensor_idx_1 *
                       rtb_FXOS87006AxesSensor_idx_1) +
                      rtb_FXOS87006AxesSensor_idx_2 *
                      rtb_FXOS87006AxesSensor_idx_2) - (real_T)
                 Hardware_Hidden_Symulink_B.Activity_Threshold >=
                 Hardware_Hidden_Symulink_P.CompareToConstant_const);

  /* Product: '<S5>/Divide' incorporates:
   *  Sum: '<S5>/Subtract1'
   */
  if (Hardware_Hidden_Symulink_B.Recovery_Time == 0U) {
    status = MAX_uint8_T;

    /* Divide by zero handler */
  } else {
    status = (uint8_T)((uint32_T)(uint8_T)
                       (Hardware_Hidden_Symulink_B.Max_Sensor_Rate -
                        Hardware_Hidden_Symulink_B.LRL) /
                       Hardware_Hidden_Symulink_B.Recovery_Time);
  }

  /* Sum: '<S11>/Sum' incorporates:
   *  Product: '<S11>/Product'
   *  Product: '<S5>/Divide'
   */
  rtb_Sum = status * Hardware_Hidden_Symulink_B.Response_Factor +
    Hardware_Hidden_Symulink_B.LRL;

  /* Chart: '<S5>/Chart' incorporates:
   *  DataTypeConversion: '<S5>/Cast To Double1'
   *  DataTypeConversion: '<S5>/Cast To Double2'
   */
  if (Hardware_Hidden_Symulink_DW.temporalCounter_i1_i < 15U) {
    Hardware_Hidden_Symulink_DW.temporalCounter_i1_i++;
  }

  if (Hardware_Hidden_Symulink_DW.is_active_c6_Hardware_Hidden_Sy == 0U) {
    Hardware_Hidden_Symulink_DW.is_active_c6_Hardware_Hidden_Sy = 1U;
    rtb_FXOS87006AxesSensor_idx_0 = rtb_Sum - Hardware_Hidden_Symulink_B.LRL;
    Hardware_Hidden_Symulink_DW.step_up = rtb_FXOS87006AxesSensor_idx_0 > 0.0 ?
      (rtInf) : rtb_FXOS87006AxesSensor_idx_0 < 0.0 ? (rtMinusInf) : (rtNaN);
    Hardware_Hidden_Symulink_DW.step_up = ceil
      (Hardware_Hidden_Symulink_DW.step_up);
    Hardware_Hidden_Symulink_DW.step_down = rtb_FXOS87006AxesSensor_idx_0 /
      (real_T)Hardware_Hidden_Symulink_B.Recovery_Time;
    Hardware_Hidden_Symulink_DW.step_down = ceil
      (Hardware_Hidden_Symulink_DW.step_down);
    Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
      Hardware_Hidden_Symul_IN_Start1;
    Hardware_Hidden_Symulink_B.AdaptedRate = Hardware_Hidden_Symulink_B.LRL;
  } else {
    switch (Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink) {
     case Hardware_Hidden_Symu_IN_S2FAIL1:
      if (Hardware_Hidden_Symulink_B.AdaptedRate <=
          Hardware_Hidden_Symulink_B.LRL) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symul_IN_Start1;
        Hardware_Hidden_Symulink_B.AdaptedRate = Hardware_Hidden_Symulink_B.LRL;
      } else if ((Hardware_Hidden_Symulink_DW.temporalCounter_i1_i >= 10U) &&
                 (Hardware_Hidden_Symulink_B.AdaptedRate >=
                  Hardware_Hidden_Symulink_B.LRL)) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symu_IN_S2FAIL1;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate -=
          Hardware_Hidden_Symulink_DW.step_down;
      } else if (rtb_Compare) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symulink_IN_S4;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate +=
          Hardware_Hidden_Symulink_DW.step_up;
      }
      break;

     case Hardware_Hidden_Symulink_IN_S3:
      if (rtb_Compare) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symulink_IN_S3;
        Hardware_Hidden_Symulink_B.AdaptedRate = rtb_Sum;
      } else {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symu_IN_S2FAIL1;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate -=
          Hardware_Hidden_Symulink_DW.step_down;
      }
      break;

     case Hardware_Hidden_Symulink_IN_S4:
      if ((Hardware_Hidden_Symulink_DW.temporalCounter_i1_i >= 10U) &&
          (Hardware_Hidden_Symulink_B.AdaptedRate <= rtb_Sum)) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symulink_IN_S4;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate +=
          Hardware_Hidden_Symulink_DW.step_up;
      } else if (!rtb_Compare) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden__IN_S_FAILSAFE1;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate -=
          Hardware_Hidden_Symulink_DW.step_up;
      } else if (Hardware_Hidden_Symulink_B.AdaptedRate >= rtb_Sum) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symulink_IN_S3;
        Hardware_Hidden_Symulink_B.AdaptedRate = rtb_Sum;
      }
      break;

     case Hardware_Hidden__IN_S_FAILSAFE1:
      if (rtb_Compare) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symulink_IN_S4;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate +=
          Hardware_Hidden_Symulink_DW.step_up;
      } else if (Hardware_Hidden_Symulink_DW.temporalCounter_i1_i >= 10U) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symu_IN_S2FAIL1;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate -=
          Hardware_Hidden_Symulink_DW.step_down;
      }
      break;

     default:
      /* case IN_Start1: */
      if (rtb_Compare) {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symulink_IN_S4;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1_i = 0U;
        Hardware_Hidden_Symulink_B.AdaptedRate +=
          Hardware_Hidden_Symulink_DW.step_up;
      } else {
        Hardware_Hidden_Symulink_DW.is_c6_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symul_IN_Start1;
        Hardware_Hidden_Symulink_B.AdaptedRate = Hardware_Hidden_Symulink_B.LRL;
      }
      break;
    }
  }

  /* End of Chart: '<S5>/Chart' */

  /* Chart: '<Root>/ states  ' incorporates:
   *  Constant: '<S5>/Constant'
   *  MATLABSystem: '<S3>/ATR_DETECT'
   *  MATLABSystem: '<S3>/VENT_DETECT'
   *  Product: '<S5>/Divide1'
   */
  if (Hardware_Hidden_Symulink_DW.temporalCounter_i1 < MAX_uint32_T) {
    Hardware_Hidden_Symulink_DW.temporalCounter_i1++;
  }

  if (Hardware_Hidden_Symulink_DW.is_active_c3_Hardware_Hidden_Sy == 0U) {
    Hardware_Hidden_Symulink_DW.is_active_c3_Hardware_Hidden_Sy = 1U;
    enter_internal_c3_Hardware_Hidd();
  } else {
    switch (Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink) {
     case Hardware_Hidden_Sym_IN_AVPacing:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.ATR_PW) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symu_IN_Inhibit;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
      }
      break;

     case Hardware_Hidden_S_IN_CharingC22:
      Hardware_Hidden_Symu_CharingC22(&tmp);
      break;

     case Hardware_Hidden_Symu_IN_Inhibit:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.ARP) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_S_IN_CharingC22;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      } else {
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
      }
      break;

     case Hardware_Hidden_S_IN_CharingC23:
      rtb_FXOS87006AxesSensor_idx_0 = rt_roundd_snf
        (Hardware_Hidden_Symulink_P.Constant_Value /
         Hardware_Hidden_Symulink_B.AdaptedRate - (real_T)
         Hardware_Hidden_Symulink_B.ATR_PW);
      if (rtb_FXOS87006AxesSensor_idx_0 < 256.0) {
        if (rtb_FXOS87006AxesSensor_idx_0 >= 0.0) {
          status = (uint8_T)rtb_FXOS87006AxesSensor_idx_0;
        } else {
          status = 0U;
        }
      } else {
        status = MAX_uint8_T;
      }

      qY = (uint32_T)status - /*MW:OvSatOk*/ Hardware_Hidden_Symulink_B.ARP;
      if (qY > status) {
        qY = 0U;
      }

      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= qY) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden__IN_DISCHARGING;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden__IN_DISCHARGING:
      qY = (uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                      100);
      if ((qY >= Hardware_Hidden_Symulink_B.ATR_PW) || ((qY >=
            Hardware_Hidden_Symulink_B.LRL) && (tmp ==
            Hardware_Hidden_Symulink_DW.HIGH))) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symuli_IN_Proxy;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
      }
      break;

     case Hardware_Hidden_Symuli_IN_Proxy:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.ARP) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_S_IN_CharingC23;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden_S_IN_AVPacing_k:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.ATR_PW) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_IN_CharingC22_c;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
      }
      break;

     case Hardware_Hidden_IN_CharingC22_c:
      Hardware_Hidden_Sy_CharingC22_p();
      break;

     case Hardware_Hidden_Sy_IN_AVPacing1:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.ATR_PW) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_IN_CharingC23_n;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden_IN_CharingC23_n:
      qY = (uint32_T)Hardware_Hidden_Symulink_B.Period - /*MW:OvSatOk*/
        Hardware_Hidden_Symulink_B.ATR_PW;
      if (qY > Hardware_Hidden_Symulink_B.Period) {
        qY = 0U;
      }

      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= qY) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_Sy_IN_AVPacing1;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.ATR_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.ATR_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.ATR_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidde_IN_CharingC23_nn:
      qY = (uint32_T)Hardware_Hidden_Symulink_B.Period - /*MW:OvSatOk*/
        Hardware_Hidden_Symulink_B.VENT_PW;
      if (qY > Hardware_Hidden_Symulink_B.Period) {
        qY = 0U;
      }

      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= qY) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_Sy_IN_Discharge;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden_Sy_IN_Discharge:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.VENT_PW) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidde_IN_CharingC23_nn;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidd_IN_CharingC23_nnr:
      qY = (uint32_T)Hardware_Hidden_Symulink_B.Period - /*MW:OvSatOk*/
        Hardware_Hidden_Symulink_B.VENT_PW;
      if (qY > Hardware_Hidden_Symulink_B.Period) {
        qY = 0U;
      }

      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= qY) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden__IN_Discharge_o;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden__IN_Discharge_o:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.VENT_PW) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidd_IN_CharingC23_nnr;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden__IN_AVPacing1_b:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.ATR_PW) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hid_IN_CharingC23_nnrd;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hid_IN_CharingC23_nnrd:
      qY = (uint32_T)Hardware_Hidden_Symulink_B.Period - /*MW:OvSatOk*/
        Hardware_Hidden_Symulink_B.ATR_PW;
      if (qY > Hardware_Hidden_Symulink_B.Period) {
        qY = 0U;
      }

      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= qY) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden__IN_AVPacing1_b;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hi_IN_CharingC23_nnrds:
      Hardware_Hidden_Symu_CharingC23(&tmp_0);
      break;

     case Hardware_Hidden_IN_Discharge_oe:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.VENT_PW) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_Sy_IN_Inhibit_o;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden_Sy_IN_Inhibit_o:
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.VRP) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hi_IN_CharingC23_nnrds;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidden_Sym_IN_CHARGING:
      rtb_FXOS87006AxesSensor_idx_0 = rt_roundd_snf
        (Hardware_Hidden_Symulink_P.Constant_Value /
         Hardware_Hidden_Symulink_B.AdaptedRate - (real_T)
         Hardware_Hidden_Symulink_B.VENT_PW);
      if (rtb_FXOS87006AxesSensor_idx_0 < 256.0) {
        if (rtb_FXOS87006AxesSensor_idx_0 >= 0.0) {
          status = (uint8_T)rtb_FXOS87006AxesSensor_idx_0;
        } else {
          status = 0U;
        }
      } else {
        status = MAX_uint8_T;
      }

      qY = (uint32_T)status - /*MW:OvSatOk*/ Hardware_Hidden_Symulink_B.VRP;
      if (qY > status) {
        qY = 0U;
      }

      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= qY) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidde_IN_DISCHARGING_f;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_REF_PWM =
          Hardware_Hidden_Symulink_B.VENT_DUTY_CYCLE;
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     case Hardware_Hidde_IN_DISCHARGING_f:
      qY = (uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                      100);
      if ((qY >= Hardware_Hidden_Symulink_B.VENT_PW) || ((qY >=
            Hardware_Hidden_Symulink_B.LRL) && (tmp_0 ==
            Hardware_Hidden_Symulink_DW.HIGH))) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_Symuli_IN_PROXY;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;

     default:
      /* case IN_PROXY: */
      if ((uint32_T)((int32_T)Hardware_Hidden_Symulink_DW.temporalCounter_i1 *
                     100) >= Hardware_Hidden_Symulink_B.VRP) {
        Hardware_Hidden_Symulink_DW.is_c3_Hardware_Hidden_Symulink =
          Hardware_Hidden_Sym_IN_CHARGING;
        Hardware_Hidden_Symulink_DW.temporalCounter_i1 = 0U;
      } else {
        Hardware_Hidden_Symulink_B.PACE_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
        Hardware_Hidden_Symulink_B.VENT_PACE_CTRL =
          Hardware_Hidden_Symulink_DW.LOW;
        Hardware_Hidden_Symulink_B.VENT_GND_CTRL =
          Hardware_Hidden_Symulink_DW.HIGH;
      }
      break;
    }
  }

  /* End of Chart: '<Root>/ states  ' */

  /* MATLABSystem: '<S6>/VENT_GND_CTRL_OUT' */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_o.MW_DIGITALIO_HANDLE,
                     Hardware_Hidden_Symulink_B.VENT_GND_CTRL);

  /* MATLABSystem: '<S6>/VENT_PACE_CTRL_OUT' */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_i.MW_DIGITALIO_HANDLE,
                     Hardware_Hidden_Symulink_B.VENT_PACE_CTRL);

  /* MATLABSystem: '<S6>/ATR_PACE_CTRL_OUT' */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_h.MW_DIGITALIO_HANDLE,
                     Hardware_Hidden_Symulink_B.ATR_PACE_CTRL);

  /* MATLABSystem: '<S6>/ATR_GND_CTRL_OUT' */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_f.MW_DIGITALIO_HANDLE,
                     Hardware_Hidden_Symulink_B.ATR_GND_CTRL);

  /* MATLABSystem: '<S6>/PACE_CHARCE_CTRL_OUT' */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_p.MW_DIGITALIO_HANDLE,
                     Hardware_Hidden_Symulink_B.PACE_CHARGE_CTRL);

  /* MATLABSystem: '<S6>/PACE_GND_CTRL_OUT' */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_ba.MW_DIGITALIO_HANDLE,
                     Hardware_Hidden_Symulink_B.PACE_GND_CTRL);

  /* MATLABSystem: '<S6>/PACE_REF_PWM_OUT' */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_k.MW_DIGITALIO_HANDLE,
                     Hardware_Hidden_Symulink_B.PACE_REF_PWM != 0);

  /* MATLABSystem: '<S4>/FRONTEND_CTRL' incorporates:
   *  MATLAB Function: '<S4>/MATLAB Function'
   */
  MW_digitalIO_write(Hardware_Hidden_Symulink_DW.obj_mo.MW_DIGITALIO_HANDLE,
                     (Hardware_Hidden_Symulink_B.Mode == 3) ||
                     (Hardware_Hidden_Symulink_B.Mode == 4) ||
                     (Hardware_Hidden_Symulink_B.Mode == 7) ||
                     (Hardware_Hidden_Symulink_B.Mode == 8));

  /* MATLABSystem: '<S4>/Atr_Sensitivity' incorporates:
   *  Constant: '<S4>/Constant1'
   */
  MW_PWM_SetDutyCycle(Hardware_Hidden_Symulink_DW.obj_l.MW_PWM_HANDLE,
                      Hardware_Hidden_Symulink_P.Constant1_Value);

  /* MATLABSystem: '<S4>/Vent_Sensitivity' incorporates:
   *  Constant: '<S4>/Constant8'
   */
  MW_PWM_SetDutyCycle(Hardware_Hidden_Symulink_DW.obj_e.MW_PWM_HANDLE,
                      Hardware_Hidden_Symulink_P.Constant8_Value);
}

/* Use this function only if you need to maintain compatibility with an existing static main program. */
void Hardware_Hidden_Symulink_step(int_T tid)
{
  switch (tid) {
   case 0 :
    Hardware_Hidden_Symulink_step0();
    break;

   case 1 :
    Hardware_Hidden_Symulink_step1();
    break;

   default :
    /* do nothing */
    break;
  }
}

/* Model initialize function */
void Hardware_Hidden_Symulink_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  {
    freedomk64f_DigitalRead_Hardw_T *obj;
    freedomk64f_DigitalWrite_Hard_T *obj_0;
    freedomk64f_PWMOutput_Hardwar_T *obj_1;

    /* SystemInitialize for S-Function (sfun_private_function_caller) generated from: '<Root>/Function-Call Subsystem' incorporates:
     *  SubSystem: '<Root>/Function-Call Subsystem'
     */
    send_param_Init();

    /* End of SystemInitialize for S-Function (sfun_private_function_caller) generated from: '<Root>/Function-Call Subsystem' */

    /* SystemInitialize for Chart: '<Root>/ states  ' */
    Hardware_Hidden_Symulink_DW.HIGH = true;

    /* Start for MATLABSystem: '<S4>/Serial Receive' */
    Hardware_Hidden_Symulink_DW.obj_m.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_m.matlabCodegenIsDeleted = false;
    Hardware_Hidden_Symulink_DW.obj_m.SampleTime =
      Hardware_Hidden_Symulink_P.SerialReceive_SampleTime;
    Hardware_Hi_SystemCore_setup_hp(&Hardware_Hidden_Symulink_DW.obj_m);

    /* Start for MATLABSystem: '<S3>/ATR_DETECT' */
    Hardware_Hidden_Symulink_DW.obj_g.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_g.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_g.SampleTime = -1.0;
    Hardware_Hidden_Symulink_DW.obj_g.matlabCodegenIsDeleted = false;
    Hardware_Hidden_Symulink_DW.obj_g.SampleTime =
      Hardware_Hidden_Symulink_P.ATR_DETECT_SampleTime;
    obj = &Hardware_Hidden_Symulink_DW.obj_g;
    Hardware_Hidden_Symulink_DW.obj_g.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_g.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(0U, 0);
    Hardware_Hidden_Symulink_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<S3>/VENT_DETECT' */
    Hardware_Hidden_Symulink_DW.obj_n2.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_n2.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_n2.SampleTime = -1.0;
    Hardware_Hidden_Symulink_DW.obj_n2.matlabCodegenIsDeleted = false;
    Hardware_Hidden_Symulink_DW.obj_n2.SampleTime =
      Hardware_Hidden_Symulink_P.VENT_DETECT_SampleTime;
    obj = &Hardware_Hidden_Symulink_DW.obj_n2;
    Hardware_Hidden_Symulink_DW.obj_n2.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_n2.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(1U, 0);
    Hardware_Hidden_Symulink_DW.obj_n2.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor' */
    Hardware_Hidden_Symulink_DW.obj.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj.i2cobj.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj.i2cobj.matlabCodegenIsDeleted = false;
    Hardware_Hidden_Symulink_DW.obj.matlabCodegenIsDeleted = false;
    Hardware_Hidden_Symulink_DW.obj.SampleTime =
      Hardware_Hidden_Symulink_P.FXOS87006AxesSensor_SampleTime;
    Hardware_Hid_SystemCore_setup_h(&Hardware_Hidden_Symulink_DW.obj);

    /* Start for MATLABSystem: '<S6>/VENT_GND_CTRL_OUT' */
    Hardware_Hidden_Symulink_DW.obj_o.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_o.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_o.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_o;
    Hardware_Hidden_Symulink_DW.obj_o.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_o.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    Hardware_Hidden_Symulink_DW.obj_o.isSetupComplete = true;

    /* Start for MATLABSystem: '<S6>/VENT_PACE_CTRL_OUT' */
    Hardware_Hidden_Symulink_DW.obj_i.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_i.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_i.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_i;
    Hardware_Hidden_Symulink_DW.obj_i.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_i.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    Hardware_Hidden_Symulink_DW.obj_i.isSetupComplete = true;

    /* Start for MATLABSystem: '<S6>/ATR_PACE_CTRL_OUT' */
    Hardware_Hidden_Symulink_DW.obj_h.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_h.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_h.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_h;
    Hardware_Hidden_Symulink_DW.obj_h.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_h.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    Hardware_Hidden_Symulink_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<S6>/ATR_GND_CTRL_OUT' */
    Hardware_Hidden_Symulink_DW.obj_f.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_f.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_f.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_f;
    Hardware_Hidden_Symulink_DW.obj_f.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_f.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    Hardware_Hidden_Symulink_DW.obj_f.isSetupComplete = true;

    /* Start for MATLABSystem: '<S6>/PACE_CHARCE_CTRL_OUT' */
    Hardware_Hidden_Symulink_DW.obj_p.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_p.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_p.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_p;
    Hardware_Hidden_Symulink_DW.obj_p.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_p.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    Hardware_Hidden_Symulink_DW.obj_p.isSetupComplete = true;

    /* Start for MATLABSystem: '<S6>/PACE_GND_CTRL_OUT' */
    Hardware_Hidden_Symulink_DW.obj_ba.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_ba.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_ba.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_ba;
    Hardware_Hidden_Symulink_DW.obj_ba.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_ba.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    Hardware_Hidden_Symulink_DW.obj_ba.isSetupComplete = true;

    /* Start for MATLABSystem: '<S6>/PACE_REF_PWM_OUT' */
    Hardware_Hidden_Symulink_DW.obj_k.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_k.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_k.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_k;
    Hardware_Hidden_Symulink_DW.obj_k.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_k.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(5U, 1);
    Hardware_Hidden_Symulink_DW.obj_k.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/FRONTEND_CTRL' */
    Hardware_Hidden_Symulink_DW.obj_mo.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_mo.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_mo.matlabCodegenIsDeleted = false;
    obj_0 = &Hardware_Hidden_Symulink_DW.obj_mo;
    Hardware_Hidden_Symulink_DW.obj_mo.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_mo.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(13U, 1);
    Hardware_Hidden_Symulink_DW.obj_mo.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/Atr_Sensitivity' */
    Hardware_Hidden_Symulink_DW.obj_l.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_l.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_l.matlabCodegenIsDeleted = false;
    obj_1 = &Hardware_Hidden_Symulink_DW.obj_l;
    Hardware_Hidden_Symulink_DW.obj_l.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_l.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(3U, 2000.0, 0.0);
    MW_PWM_Start(Hardware_Hidden_Symulink_DW.obj_l.MW_PWM_HANDLE);
    Hardware_Hidden_Symulink_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/Vent_Sensitivity' */
    Hardware_Hidden_Symulink_DW.obj_e.matlabCodegenIsDeleted = true;
    Hardware_Hidden_Symulink_DW.obj_e.isInitialized = 0;
    Hardware_Hidden_Symulink_DW.obj_e.matlabCodegenIsDeleted = false;
    obj_1 = &Hardware_Hidden_Symulink_DW.obj_e;
    Hardware_Hidden_Symulink_DW.obj_e.isSetupComplete = false;
    Hardware_Hidden_Symulink_DW.obj_e.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(6U, 2000.0, 0.0);
    MW_PWM_Start(Hardware_Hidden_Symulink_DW.obj_e.MW_PWM_HANDLE);
    Hardware_Hidden_Symulink_DW.obj_e.isSetupComplete = true;
  }
}

/* Model terminate function */
void Hardware_Hidden_Symulink_terminate(void)
{
  b_freedomk64f_I2CMasterWrite__T *obj;

  /* Terminate for MATLABSystem: '<S4>/Serial Receive' */
  if (!Hardware_Hidden_Symulink_DW.obj_m.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_m.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_m.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_m.isSetupComplete) {
      MW_SCI_Close(Hardware_Hidden_Symulink_DW.obj_m.MW_SCIHANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S4>/Serial Receive' */

  /* Terminate for S-Function (sfun_private_function_caller) generated from: '<Root>/Function-Call Subsystem' incorporates:
   *  SubSystem: '<Root>/Function-Call Subsystem'
   */
  send_param_Term();

  /* End of Terminate for S-Function (sfun_private_function_caller) generated from: '<Root>/Function-Call Subsystem' */

  /* Terminate for MATLABSystem: '<S3>/ATR_DETECT' */
  if (!Hardware_Hidden_Symulink_DW.obj_g.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_g.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_g.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_g.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_g.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/ATR_DETECT' */

  /* Terminate for MATLABSystem: '<S3>/VENT_DETECT' */
  if (!Hardware_Hidden_Symulink_DW.obj_n2.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_n2.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_n2.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_n2.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_n2.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S3>/VENT_DETECT' */

  /* Terminate for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor' */
  if (!Hardware_Hidden_Symulink_DW.obj.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj.isSetupComplete) {
      MW_I2C_Close(Hardware_Hidden_Symulink_DW.obj.i2cobj.MW_I2C_HANDLE);
    }
  }

  obj = &Hardware_Hidden_Symulink_DW.obj.i2cobj;
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    if (obj->isInitialized == 1) {
      obj->isInitialized = 2;
    }
  }

  /* End of Terminate for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor' */

  /* Terminate for MATLABSystem: '<S6>/VENT_GND_CTRL_OUT' */
  if (!Hardware_Hidden_Symulink_DW.obj_o.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_o.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_o.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_o.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_o.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S6>/VENT_GND_CTRL_OUT' */

  /* Terminate for MATLABSystem: '<S6>/VENT_PACE_CTRL_OUT' */
  if (!Hardware_Hidden_Symulink_DW.obj_i.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_i.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_i.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_i.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_i.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S6>/VENT_PACE_CTRL_OUT' */

  /* Terminate for MATLABSystem: '<S6>/ATR_PACE_CTRL_OUT' */
  if (!Hardware_Hidden_Symulink_DW.obj_h.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_h.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_h.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_h.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_h.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S6>/ATR_PACE_CTRL_OUT' */

  /* Terminate for MATLABSystem: '<S6>/ATR_GND_CTRL_OUT' */
  if (!Hardware_Hidden_Symulink_DW.obj_f.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_f.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_f.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_f.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_f.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S6>/ATR_GND_CTRL_OUT' */

  /* Terminate for MATLABSystem: '<S6>/PACE_CHARCE_CTRL_OUT' */
  if (!Hardware_Hidden_Symulink_DW.obj_p.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_p.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_p.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_p.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_p.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S6>/PACE_CHARCE_CTRL_OUT' */

  /* Terminate for MATLABSystem: '<S6>/PACE_GND_CTRL_OUT' */
  if (!Hardware_Hidden_Symulink_DW.obj_ba.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_ba.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_ba.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_ba.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_ba.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S6>/PACE_GND_CTRL_OUT' */

  /* Terminate for MATLABSystem: '<S6>/PACE_REF_PWM_OUT' */
  if (!Hardware_Hidden_Symulink_DW.obj_k.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_k.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_k.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_k.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_k.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S6>/PACE_REF_PWM_OUT' */

  /* Terminate for MATLABSystem: '<S4>/FRONTEND_CTRL' */
  if (!Hardware_Hidden_Symulink_DW.obj_mo.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_mo.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_mo.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_mo.isSetupComplete) {
      MW_digitalIO_close(Hardware_Hidden_Symulink_DW.obj_mo.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S4>/FRONTEND_CTRL' */

  /* Terminate for MATLABSystem: '<S4>/Atr_Sensitivity' */
  if (!Hardware_Hidden_Symulink_DW.obj_l.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_l.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_l.isSetupComplete) {
      MW_PWM_Stop(Hardware_Hidden_Symulink_DW.obj_l.MW_PWM_HANDLE);
      MW_PWM_Close(Hardware_Hidden_Symulink_DW.obj_l.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S4>/Atr_Sensitivity' */

  /* Terminate for MATLABSystem: '<S4>/Vent_Sensitivity' */
  if (!Hardware_Hidden_Symulink_DW.obj_e.matlabCodegenIsDeleted) {
    Hardware_Hidden_Symulink_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((Hardware_Hidden_Symulink_DW.obj_e.isInitialized == 1) &&
        Hardware_Hidden_Symulink_DW.obj_e.isSetupComplete) {
      MW_PWM_Stop(Hardware_Hidden_Symulink_DW.obj_e.MW_PWM_HANDLE);
      MW_PWM_Close(Hardware_Hidden_Symulink_DW.obj_e.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S4>/Vent_Sensitivity' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
