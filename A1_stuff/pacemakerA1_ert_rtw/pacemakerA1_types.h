/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: pacemakerA1_types.h
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

#ifndef RTW_HEADER_pacemakerA1_types_h_
#define RTW_HEADER_pacemakerA1_types_h_
#include "rtwtypes.h"
#include "MW_SVD.h"

/* Model Code Variants */

/* Custom Type definition for MATLABSystem: '<S2>/Digital Write8' */
#include "MW_SVD.h"
#ifndef struct_tag_0QIIqIWUIOhUbf1p9QN9pB
#define struct_tag_0QIIqIWUIOhUbf1p9QN9pB

struct tag_0QIIqIWUIOhUbf1p9QN9pB
{
  int32_T __dummy;
};

#endif                                 /* struct_tag_0QIIqIWUIOhUbf1p9QN9pB */

#ifndef typedef_b_freedomk64f_Hardware_pacema_T
#define typedef_b_freedomk64f_Hardware_pacema_T

typedef struct tag_0QIIqIWUIOhUbf1p9QN9pB b_freedomk64f_Hardware_pacema_T;

#endif                             /* typedef_b_freedomk64f_Hardware_pacema_T */

#ifndef struct_tag_EkIWEs70Gs0LyfeXELZ2TC
#define struct_tag_EkIWEs70Gs0LyfeXELZ2TC

struct tag_EkIWEs70Gs0LyfeXELZ2TC
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_pacema_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
};

#endif                                 /* struct_tag_EkIWEs70Gs0LyfeXELZ2TC */

#ifndef typedef_freedomk64f_DigitalWrite_pace_T
#define typedef_freedomk64f_DigitalWrite_pace_T

typedef struct tag_EkIWEs70Gs0LyfeXELZ2TC freedomk64f_DigitalWrite_pace_T;

#endif                             /* typedef_freedomk64f_DigitalWrite_pace_T */

/* Parameters (default storage) */
typedef struct P_pacemakerA1_T_ P_pacemakerA1_T;

/* Forward declaration for rtModel */
typedef struct tag_RTM_pacemakerA1_T RT_MODEL_pacemakerA1_T;

#endif                                 /* RTW_HEADER_pacemakerA1_types_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
