/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Hardware_Hidden_Symulink.h
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

#ifndef RTW_HEADER_Hardware_Hidden_Symulink_h_
#define RTW_HEADER_Hardware_Hidden_Symulink_h_
#ifndef Hardware_Hidden_Symulink_COMMON_INCLUDES_
#define Hardware_Hidden_Symulink_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#include "MW_I2C.h"
#include "MW_SCI.h"
#include "MW_AnalogIn.h"
#endif                           /* Hardware_Hidden_Symulink_COMMON_INCLUDES_ */

#include "Hardware_Hidden_Symulink_types.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#include "rtGetNaN.h"
#include <stddef.h>
#include "send_param.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

#ifndef rtmStepTask
#define rtmStepTask(rtm, idx)          ((rtm)->Timing.TaskCounters.TID[(idx)] == 0)
#endif

#ifndef rtmTaskCounter
#define rtmTaskCounter(rtm, idx)       ((rtm)->Timing.TaskCounters.TID[(idx)])
#endif

/* Block signals (default storage) */
typedef struct {
  uint8_T TxDataLocChar[88];
  real_T TmpSignalConversionAtSerial[11];
  uint8_T RxData[19];
  uint8_T RxDataLocChar[19];
  uint32_T TxPinLoc;
  uint32_T SCIModuleLoc;
  MW_SCI_StopBits_Type StopBitsValue;
  MW_SCI_Parity_Type ParityValue;
  MW_I2C_Mode_Type ModeType;
  uint32_T i2cname;
  real_T AdaptedRate;                  /* '<S5>/Chart' */
  uint8_T b_SwappedDataBytes[2];
  uint8_T ATR_DUTY_CYCLE;              /* '<S4>/Chart' */
  uint8_T LRL;                         /* '<S4>/Chart' */
  uint8_T ATR_PW;                      /* '<S4>/Chart' */
  uint8_T Mode;                        /* '<S4>/Chart' */
  uint8_T ARP;                         /* '<S4>/Chart' */
  uint8_T VENT_DUTY_CYCLE;             /* '<S4>/Chart' */
  uint8_T VENT_PW;                     /* '<S4>/Chart' */
  uint8_T VRP;                         /* '<S4>/Chart' */
  uint8_T Activity_Threshold;          /* '<S4>/Chart' */
  uint8_T Max_Sensor_Rate;             /* '<S4>/Chart' */
  uint8_T Recovery_Time;               /* '<S4>/Chart' */
  uint8_T Response_Factor;             /* '<S4>/Chart' */
  uint8_T Period;                      /* '<S4>/Chart' */
  uint8_T PACE_REF_PWM;                /* '<Root>/ states  ' */
  uint8_T b_RegisterValue;
  uint8_T status;
  boolean_T VENT_GND_CTRL;             /* '<Root>/ states  ' */
  boolean_T VENT_PACE_CTRL;            /* '<Root>/ states  ' */
  boolean_T ATR_PACE_CTRL;             /* '<Root>/ states  ' */
  boolean_T ATR_GND_CTRL;              /* '<Root>/ states  ' */
  boolean_T PACE_CHARGE_CTRL;          /* '<Root>/ states  ' */
  boolean_T PACE_GND_CTRL;             /* '<Root>/ states  ' */
} B_Hardware_Hidden_Symulink_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_fxos8700_Hardware_T obj; /* '<S4>/FXOS8700 6-Axes Sensor' */
  freedomk64f_AnalogInput_Hardw_T obj_j;/* '<S2>/Ventricle egram' */
  freedomk64f_AnalogInput_Hardw_T obj_n;/* '<S2>/Atrium egram' */
  freedomk64f_DigitalRead_Hardw_T obj_n2;/* '<S3>/VENT_DETECT' */
  freedomk64f_DigitalRead_Hardw_T obj_g;/* '<S3>/ATR_DETECT' */
  freedomk64f_SCIRead_Hardware__T obj_m;/* '<S4>/Serial Receive' */
  freedomk64f_SCIWrite_Hardware_T obj_b;/* '<S2>/Serial Transmit' */
  freedomk64f_PWMOutput_Hardwar_T obj_e;/* '<S4>/Vent_Sensitivity' */
  freedomk64f_PWMOutput_Hardwar_T obj_l;/* '<S4>/Atr_Sensitivity' */
  freedomk64f_DigitalWrite_Hard_T obj_i;/* '<S6>/VENT_PACE_CTRL_OUT' */
  freedomk64f_DigitalWrite_Hard_T obj_o;/* '<S6>/VENT_GND_CTRL_OUT' */
  freedomk64f_DigitalWrite_Hard_T obj_k;/* '<S6>/PACE_REF_PWM_OUT' */
  freedomk64f_DigitalWrite_Hard_T obj_ba;/* '<S6>/PACE_GND_CTRL_OUT' */
  freedomk64f_DigitalWrite_Hard_T obj_p;/* '<S6>/PACE_CHARCE_CTRL_OUT' */
  freedomk64f_DigitalWrite_Hard_T obj_h;/* '<S6>/ATR_PACE_CTRL_OUT' */
  freedomk64f_DigitalWrite_Hard_T obj_f;/* '<S6>/ATR_GND_CTRL_OUT' */
  freedomk64f_DigitalWrite_Hard_T obj_mo;/* '<S4>/FRONTEND_CTRL' */
  real_T step_down;                    /* '<S5>/Chart' */
  real_T step_up;                      /* '<S5>/Chart' */
  uint32_T temporalCounter_i1;         /* '<Root>/ states  ' */
  uint8_T is_active_c6_Hardware_Hidden_Sy;/* '<S5>/Chart' */
  uint8_T is_c6_Hardware_Hidden_Symulink;/* '<S5>/Chart' */
  uint8_T temporalCounter_i1_i;        /* '<S5>/Chart' */
  uint8_T is_active_c1_Hardware_Hidden_Sy;/* '<S4>/Chart' */
  uint8_T is_c1_Hardware_Hidden_Symulink;/* '<S4>/Chart' */
  uint8_T is_active_c3_Hardware_Hidden_Sy;/* '<Root>/ states  ' */
  uint8_T is_c3_Hardware_Hidden_Symulink;/* '<Root>/ states  ' */
  boolean_T HIGH;                      /* '<Root>/ states  ' */
  boolean_T LOW;                       /* '<Root>/ states  ' */
} DW_Hardware_Hidden_Symulink_T;

/* Parameters (default storage) */
struct P_Hardware_Hidden_Symulink_T_ {
  real_T CompareToConstant_const;     /* Mask Parameter: CompareToConstant_const
                                       * Referenced by: '<S10>/Constant'
                                       */
  real_T ATR_DETECT_SampleTime;        /* Expression: SampleTime
                                        * Referenced by: '<S3>/ATR_DETECT'
                                        */
  real_T VENT_DETECT_SampleTime;       /* Expression: SampleTime
                                        * Referenced by: '<S3>/VENT_DETECT'
                                        */
  real_T FXOS87006AxesSensor_SampleTime;/* Expression: -1
                                         * Referenced by: '<S4>/FXOS8700 6-Axes Sensor'
                                         */
  real_T SerialReceive_SampleTime;     /* Expression: 0.1
                                        * Referenced by: '<S4>/Serial Receive'
                                        */
  real_T Atriumegram_SampleTime;       /* Expression: SampleTime
                                        * Referenced by: '<S2>/Atrium egram'
                                        */
  real_T Ventricleegram_SampleTime;    /* Expression: SampleTime
                                        * Referenced by: '<S2>/Ventricle egram'
                                        */
  real_T Constant_Value;               /* Expression: 30000
                                        * Referenced by: '<S5>/Constant'
                                        */
  real_T Constant1_Value;              /* Expression: 60
                                        * Referenced by: '<S4>/Constant1'
                                        */
  real_T Constant8_Value;              /* Expression: 60
                                        * Referenced by: '<S4>/Constant8'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_Hardware_Hidden_Symul_T {
  const char_T * volatile errorStatus;

  /*
   * Timing:
   * The following substructure contains information regarding
   * the timing information for the model.
   */
  struct {
    struct {
      uint8_T TID[2];
    } TaskCounters;
  } Timing;
};

/* Block parameters (default storage) */
extern P_Hardware_Hidden_Symulink_T Hardware_Hidden_Symulink_P;

/* Block signals (default storage) */
extern B_Hardware_Hidden_Symulink_T Hardware_Hidden_Symulink_B;

/* Block states (default storage) */
extern DW_Hardware_Hidden_Symulink_T Hardware_Hidden_Symulink_DW;

/* External function called from main */
extern void Hardware_Hidden_Symulink_SetEventsForThisBaseStep(boolean_T
  *eventFlags);

/* Model entry point functions */
extern void Hardware_Hidden_Symulink_SetEventsForThisBaseStep(boolean_T
  *eventFlags);
extern void Hardware_Hidden_Symulink_initialize(void);
extern void Hardware_Hidden_Symulink_step0(void);
extern void Hardware_Hidden_Symulink_step1(void);
extern void Hardware_Hidden_Symulink_step(int_T tid);
extern void Hardware_Hidden_Symulink_terminate(void);

/* Real-time Model object */
extern RT_MODEL_Hardware_Hidden_Symu_T *const Hardware_Hidden_Symulink_M;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<S3>/Cast1' : Eliminate redundant data type conversion
 * Block '<S3>/Cast2' : Eliminate redundant data type conversion
 * Block '<S5>/Cast To Double3' : Eliminate redundant data type conversion
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'Hardware_Hidden_Symulink'
 * '<S1>'   : 'Hardware_Hidden_Symulink/ states  '
 * '<S2>'   : 'Hardware_Hidden_Symulink/Function-Call Subsystem'
 * '<S3>'   : 'Hardware_Hidden_Symulink/Hardware_in'
 * '<S4>'   : 'Hardware_Hidden_Symulink/Inputs'
 * '<S5>'   : 'Hardware_Hidden_Symulink/Subsystem'
 * '<S6>'   : 'Hardware_Hidden_Symulink/out '
 * '<S7>'   : 'Hardware_Hidden_Symulink/Inputs/Chart'
 * '<S8>'   : 'Hardware_Hidden_Symulink/Inputs/MATLAB Function'
 * '<S9>'   : 'Hardware_Hidden_Symulink/Subsystem/Chart'
 * '<S10>'  : 'Hardware_Hidden_Symulink/Subsystem/Compare To Constant'
 * '<S11>'  : 'Hardware_Hidden_Symulink/Subsystem/Multiply-Add'
 */
#endif                              /* RTW_HEADER_Hardware_Hidden_Symulink_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
