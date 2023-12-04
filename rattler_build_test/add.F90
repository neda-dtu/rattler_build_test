module fort_add
    implicit none

    private
    public :: add

    contains

    subroutine add(a, b, npoints, rslt, ierror)

        implicit none

        integer, intent(in) :: npoints
        real, intent(in), dimension(npoints) :: a
        real, intent(in), dimension(npoints) :: b
        real, intent(out), dimension(npoints) :: rslt
        integer, intent(out), dimension(npoints) :: ierror

        rslt = 0.0
        ierror = 0

        rslt = a + b

    end subroutine add

end module fort_add