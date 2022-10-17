/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: pacemakerA1.h
 *
 * Code generated for Simulink model 'pacemakerA1'.
 *
 * Model version                  : 1.18
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Mon Oct 17 15:41:28 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_pacemakerA1_h_
#define RTW_HEADER_pacemakerA1_h_
#ifndef pacemakerA1_COMMON_INCLUDES_
#define pacemakerA1_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#endif                                 /* pacemakerA1_COMMON_INCLUDES_ */

#include "pacemakerA1_types.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  real_T PACE_REF_PWM;                 /* '<Root>/STATE' */
  boolean_T ATR_GND_CTRL;              /* '<Root>/STATE' */
  boolean_T PACE_CHARGE_CTRL;          /* '<Root>/STATE' */
  boolean_T ATR_PACE_CTRL;             /* '<Root>/STATE' */
  boolean_T PACE_GND_CTRL;             /* '<Root>/STATE' */
  boolean_T VENT_GND_CTRL;             /* '<Root>/STATE' */
  boolean_T VENT_PACE_CTRL;            /* '<Root>/STATE' */
  boolean_T Z_VENT_CTRL;               /* '<Root>/STATE' */
  boolean_T Z_ATR_CTRL;                /* '<Root>/STATE' */
} B_pacemakerA1_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalWrite_pace_T obj; /* '<S2>/Digital Write8' */
  freedomk64f_DigitalWrite_pace_T obj_k;/* '<S2>/Digital Write7' */
  freedomk64f_DigitalWrite_pace_T obj_p;/* '<S2>/Digital Write6' */
  freedomk64f_DigitalWrite_pace_T obj_m;/* '<S2>/Digital Write5' */
  freedomk64f_DigitalWrite_pace_T obj_f;/* '<S2>/Digital Write4' */
  freedomk64f_DigitalWrite_pace_T obj_e;/* '<S2>/Digital Write3' */
  freedomk64f_DigitalWrite_pace_T obj_l;/* '<S2>/Digital Write2' */
  freedomk64f_DigitalWrite_pace_T obj_j;/* '<S2>/Digital Write1' */
  freedomk64f_DigitalWrite_pace_T obj_h;/* '<S2>/Digital Write' */
  uint32_T temporalCounter_i1;         /* '<Root>/STATE' */
  uint8_T is_active_c3_pacemakerA1;    /* '<Root>/STATE' */
  uint8_T is_c3_pacemakerA1;           /* '<Root>/STATE' */
  boolean_T HIGH;                      /* '<Root>/STATE' */
  boolean_T LOW;                       /* '<Root>/STATE' */
} DW_pacemakerA1_T;

/* Parameters (default storage) */
struct P_pacemakerA1_T_ {
  real_T Constant1_Value;              /* Expression: 500
                                        * Referenced by: '<Root>/Constant1'
                                        */
  real_T Constant_Value;               /* Expression: 1
                                        * Referenced by: '<Root>/Constant'
                                        */
  real_T Constant2_Value;              /* Expression: 60000
                                        * Referenced by: '<Root>/Constant2'
                                        */
  real_T Constant4_Value;              /* Expression: 60
                                        * Referenced by: '<Root>/Constant4'
                                        */
  real_T Constant3_Value;              /* Expression: 2
                                        * Referenced by: '<Root>/Constant3'
                                        */
  real_T Constant5_Value;              /* Expression: 10
                                        * Referenced by: '<Root>/Constant5'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_pacemakerA1_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_pacemakerA1_T pacemakerA1_P;

/* Block signals (default storage) */
extern B_pacemakerA1_T pacemakerA1_B;

/* Block states (default storage) */
extern DW_pacemakerA1_T pacemakerA1_DW;

/* Model entry point functions */
extern void pacemakerA1_initialize(void);
extern void pacemakerA1_step(void);
extern void pacemakerA1_terminate(void);

/* Real-time Model object */
extern RT_MODEL_pacemakerA1_T *const pacemakerA1_M;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<S2>/Scope' : Unused code path elimination
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
 * '<Root>' : 'pacemakerA1'
 * '<S1>'   : 'pacemakerA1/STATE'
 * '<S2>'   : 'pacemakerA1/Subsystem'
 */
#endif                                 /* RTW_HEADER_pacemakerA1_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
