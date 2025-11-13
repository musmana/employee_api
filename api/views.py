class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()   # ➤ ADD THIS LINE
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        department_id = self.request.query_params.get('department')

        if department_id:
            queryset = queryset.filter(department__id=department_id)

        return queryset
