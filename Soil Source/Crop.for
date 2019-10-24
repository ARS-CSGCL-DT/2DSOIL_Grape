      Subroutine Crop()
      Include 'Public.ins'
      Include 'puplant.ins'
      real difx, dify, Yr(NumNP),root1 root2,M  
      Character*12 VarietyName
c initialize here      
      If (lInput.eq.1) then
       open(40,File=VarietyFile,err=10)
        read(40,*) VarietyName, LAI
        close(40)    
        cec=0.65
        nShoot=1
        isGerminated=1
        RootsInitiated=0 ! need to do initiation in carbon partitioning
        ET_demand=2.5 !just a stub for now, need to get this from weather.
        Convr=1.0   ! conversion efficiency for new roots
        
        PCRQ=0.0
        PCRL=0.0 ! no carbon for root growth
c        initialize roots 
        difx = 20.0
        dify = 55.0
        M=50.0
        rootTime=100  ! assume a fully developed root system
        COVER=1.0 - exp (-CEC*LAI)
        Do i= 1, NumNP
         
         Yr(i)=  y(1)-y(i)  ! 0 is relative to bottom in grid but must be relative to the surface for root calcs
         root2=1.0/(4.0*rootTime)*(x(i)*x(i)/difx+y(i)*y(i)/dify)
         root1 = M / (4.0 * 3.1415 * rootTime * Sqrt(difx * dify))
         RTWT(i) = root1*Exp(-root2)
       End Do
      End If
        ET_demand=2.5 !just a stub for now, need to get this from weather.
c     TPot is g plant-1 day-1, ET_demand should be g m-2 day
c     1/poprow*100/Rowsp converts to g m-2 day-1
      ET_Demand=TPot/poprow*100/RowSp
      Return
10    stop "error in crop file"      
      End
      