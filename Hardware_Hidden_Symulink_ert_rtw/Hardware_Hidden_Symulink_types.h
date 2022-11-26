/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Hardware_Hidden_Symulink_types.h
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

#ifndef RTW_HEADER_Hardware_Hidden_Symulink_types_h_
#define RTW_HEADER_Hardware_Hidden_Symulink_types_h_
#include "rtwtypes.h"
#include "MW_SVD.h"

/* Model Code Variants */

/* Custom Type definition for MATLABSystem: '<S2>/Ventricle egram' */
#include "MW_SVD.h"
#ifndef struct_tag_0QIIqIWUIOhUbf1p9QN9pB
#define struct_tag_0QIIqIWUIOhUbf1p9QN9pB

struct tag_0QIIqIWUIOhUbf1p9QN9pB
{
  int32_T __dummy;
};

#endif                                 /* struct_tag_0QIIqIWUIOhUbf1p9QN9pB */

#ifndef typedef_b_freedomk64f_Hardware_Hardwa_T
#define typedef_b_freedomk64f_Hardware_Hardwa_T

typedef struct tag_0QIIqIWUIOhUbf1p9QN9pB b_freedomk64f_Hardware_Hardwa_T;

#endif                             /* typedef_b_freedomk64f_Hardware_Hardwa_T */

#ifndef struct_tag_s1eQZAg8cMgwN6kxxyzYvC
#define struct_tag_s1eQZAg8cMgwN6kxxyzYvC

struct tag_s1eQZAg8cMgwN6kxxyzYvC
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Hardwa_T Hw;
  MW_Handle_Type MW_ANALOGIN_HANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_s1eQZAg8cMgwN6kxxyzYvC */

#ifndef typedef_freedomk64f_AnalogInput_Hardw_T
#define typedef_freedomk64f_AnalogInput_Hardw_T

typedef struct tag_s1eQZAg8cMgwN6kxxyzYvC freedomk64f_AnalogInput_Hardw_T;

#endif                             /* typedef_freedomk64f_AnalogInput_Hardw_T */

#ifndef struct_tag_GV9UedAE1zOVNNbkXknChB
#define struct_tag_GV9UedAE1zOVNNbkXknChB

struct tag_GV9UedAE1zOVNNbkXknChB
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Hardwa_T Hw;
  MW_Handle_Type MW_SCIHANDLE;
};

#endif                                 /* struct_tag_GV9UedAE1zOVNNbkXknChB */

#ifndef typedef_freedomk64f_SCIWrite_Hardware_T
#define typedef_freedomk64f_SCIWrite_Hardware_T

typedef struct tag_GV9UedAE1zOVNNbkXknChB freedomk64f_SCIWrite_Hardware_T;

#endif                             /* typedef_freedomk64f_SCIWrite_Hardware_T */

/* Custom Type definition for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor' */
#include "MW_I2C.h"
#ifndef struct_tag_q6HQSF2nXq6EjCNj0vbuLD
#define struct_tag_q6HQSF2nXq6EjCNj0vbuLD

struct tag_q6HQSF2nXq6EjCNj0vbuLD
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Hardwa_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_q6HQSF2nXq6EjCNj0vbuLD */

#ifndef typedef_freedomk64f_DigitalRead_Hardw_T
#define typedef_freedomk64f_DigitalRead_Hardw_T

typedef struct tag_q6HQSF2nXq6EjCNj0vbuLD freedomk64f_DigitalRead_Hardw_T;

#endif                             /* typedef_freedomk64f_DigitalRead_Hardw_T */

#ifndef struct_tag_RYgVoAXTz61tXGMaBAGv7F
#define struct_tag_RYgVoAXTz61tXGMaBAGv7F

struct tag_RYgVoAXTz61tXGMaBAGv7F
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Hardwa_T Hw;
  MW_Handle_Type MW_PWM_HANDLE;
};

#endif                                 /* struct_tag_RYgVoAXTz61tXGMaBAGv7F */

#ifndef typedef_freedomk64f_PWMOutput_Hardwar_T
#define typedef_freedomk64f_PWMOutput_Hardwar_T

typedef struct tag_RYgVoAXTz61tXGMaBAGv7F freedomk64f_PWMOutput_Hardwar_T;

#endif                             /* typedef_freedomk64f_PWMOutput_Hardwar_T */

#ifndef struct_tag_EkIWEs70Gs0LyfeXELZ2TC
#define struct_tag_EkIWEs70Gs0LyfeXELZ2TC

struct tag_EkIWEs70Gs0LyfeXELZ2TC
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Hardwa_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
};

#endif                                 /* struct_tag_EkIWEs70Gs0LyfeXELZ2TC */

#ifndef typedef_freedomk64f_DigitalWrite_Hard_T
#define typedef_freedomk64f_DigitalWrite_Hard_T

typedef struct tag_EkIWEs70Gs0LyfeXELZ2TC freedomk64f_DigitalWrite_Hard_T;

#endif                             /* typedef_freedomk64f_DigitalWrite_Hard_T */

#ifndef struct_tag_O0UAiliRyLLAe38ibfdAhE
#define struct_tag_O0UAiliRyLLAe38ibfdAhE

struct tag_O0UAiliRyLLAe38ibfdAhE
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  b_freedomk64f_Hardware_Hardwa_T Hw;
  uint32_T BusSpeed;
  MW_Handle_Type MW_I2C_HANDLE;
};

#endif                                 /* struct_tag_O0UAiliRyLLAe38ibfdAhE */

#ifndef typedef_b_freedomk64f_I2CMasterWrite__T
#define typedef_b_freedomk64f_I2CMasterWrite__T

typedef struct tag_O0UAiliRyLLAe38ibfdAhE b_freedomk64f_I2CMasterWrite__T;

#endif                             /* typedef_b_freedomk64f_I2CMasterWrite__T */

#ifndef struct_tag_v5Zyp5raUQrCF4f9Ln2EwE
#define struct_tag_v5Zyp5raUQrCF4f9Ln2EwE

struct tag_v5Zyp5raUQrCF4f9Ln2EwE
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  real_T SampleTime;
  b_freedomk64f_I2CMasterWrite__T i2cobj;
};

#endif                                 /* struct_tag_v5Zyp5raUQrCF4f9Ln2EwE */

#ifndef typedef_freedomk64f_fxos8700_Hardware_T
#define typedef_freedomk64f_fxos8700_Hardware_T

typedef struct tag_v5Zyp5raUQrCF4f9Ln2EwE freedomk64f_fxos8700_Hardware_T;

#endif                             /* typedef_freedomk64f_fxos8700_Hardware_T */

#ifndef struct_tag_214cR1nKZWaoqoq0FTtOUH
#define struct_tag_214cR1nKZWaoqoq0FTtOUH

struct tag_214cR1nKZWaoqoq0FTtOUH
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Hardwa_T Hw;
  MW_Handle_Type MW_SCIHANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_214cR1nKZWaoqoq0FTtOUH */

#ifndef typedef_freedomk64f_SCIRead_Hardware__T
#define typedef_freedomk64f_SCIRead_Hardware__T

typedef struct tag_214cR1nKZWaoqoq0FTtOUH freedomk64f_SCIRead_Hardware__T;

#endif                             /* typedef_freedomk64f_SCIRead_Hardware__T */

/* Parameters (default storage) */
typedef struct P_Hardware_Hidden_Symulink_T_ P_Hardware_Hidden_Symulink_T;

/* Forward declaration for rtModel */
typedef struct tag_RTM_Hardware_Hidden_Symul_T RT_MODEL_Hardware_Hidden_Symu_T;

#endif                        /* RTW_HEADER_Hardware_Hidden_Symulink_types_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
