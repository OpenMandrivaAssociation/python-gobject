%define oname pygobject
%define name python-gobject
%define version 2.13.1
%define release %mkrel 2

%if %mdkversion < 200610
%define py_platsitedir %_libdir/python%pyver/site-packages/
%endif

Summary: GObject Python bindings 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/pygobject/%{oname}-%{version}.tar.bz2
Patch: pygobject-2.11.0-fixdetection.patch
License: LGPL
Group: Development/Python
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: automake1.8
Conflicts: pygtk2.0 < 2.8.3

%description
This archive contains bindings for the GObject, to be used in Python
It is a fairly complete set of bindings, it's already rather useful, 
and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).


%prep
%setup -q -n %oname-%version
%patch -p1

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%py_platsitedir/pygtk*
%py_platsitedir/gtk-2.0/
%_libdir/pkgconfig/*.pc
%_includedir/pygtk-2.0/
%_datadir/pygobject/
%_datadir/gtk-doc/html/pygobject/


