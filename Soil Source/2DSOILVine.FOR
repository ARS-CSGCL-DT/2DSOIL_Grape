*||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||*
*                                                                      *
*     2DSOIL  - Numerical model of two-dimensional soil environment    *
*                           for field crops                            *
*                                                                      *
*                              Release 1.1.4                              *
c||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||*
      Include 'public.ins'
      include 'puplant.ins'
      Include 'Puweath.ins'
C      Include 'Nitvar.ins'

      character*132 RunDat
      integer len, status
      RunFile="Run.Dat"
      Call get_command_argument(1, RunDat, len, status)
      if (len.gt.0) then
        RunFile=RunDat
      endif

       Call Initialize()
       Call Get_Grid_and_Boundary()

 1     Call Synchronizer()

C
C SetSurfaceD --  reading daily weather
C SetSurfaceH --  reading hourly weather

      if ((HourlyWeather+DailyWeather.gt.1).or.
     &   ((HourlyWeather+DailyWeather).eq.0))then
              Write (*,*) "error in weather file type"
      Endif

      if (HourlyWeather.eq.1) Call SetSurfaceH()
      if (DailyWeather.eq.1) Call SetSurfaceD()

      Call SetTDB()
      Call CROP()
      Call Carbon_Partitioning_New()
      Call Root_diff_New()
      call Root_Mover_New()
      write(*, *) "Calling WaterUptake_New"
      Call WaterUptake_New()
      write(*,*) 'Return from WaterUptake_New'
C$$$$$$       Call WaterMover_New()
C$$$$$$       if (outputSoilYes.gt.0) then
C$$$$$$          Call Output()
C$$$$$$       endif
C$$$$$$
C$$$$$$
C$$$$$$         Goto 1
      End
