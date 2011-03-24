%define oname pygobject
%define name python-gobject
%define version 2.28.3
%define release %mkrel 2

%define api 2.0
%define major 0
%define libname %mklibname pyglib %api %major
Summary: GObject Python bindings 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/pygobject/%{oname}-%{version}.tar.bz2
Patch: pygobject-2.16.1-fixdetection.patch
Patch3: pygobject-2.28.2-fix-link.patch
License: LGPLv2+
Group: Development/Python
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: glib2-devel >= 2.24.0
BuildRequires: ffi5-devel
BuildRequires: gobject-introspection-devel >= 0.10.2
BuildRequires: python-cairo-devel
BuildRequires: gtk-doc
BuildRequires: automake
Conflicts: pygtk2.0 < 2.8.3
Requires: python-cairo

%description
This archive contains bindings for the GObject, to be used in Python
It is a fairly complete set of bindings, it's already rather useful, 
and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).

%package -n %libname
Group: System/Libraries
Summary: Python Glib bindings shared library

%description -n %libname
This archive contains bindings for the GObject, to be used in Python
It is a fairly complete set of bindings, it's already rather useful, 
and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).

%package devel
Group: Development/C
Summary: Python-gobject development files
Requires: %name = %version-%release
Requires: %libname = %version-%release
#gw requires.private in the pkg-config file
Requires: ffi5-devel

%description devel
This contains the python-gobject development files, including C
header, pkg-config file, gtk-doc generated API documentation and a code
generation tool.


%prep
%setup -q -n %oname-%version
%patch -p1 -b .fixdetection
%patch3 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
#gw this must be executable, it is used for building docs, e.g. in pyclutter
chmod 755 %buildroot%_datadir/pygobject/xsl/fixxref.py

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%py_platsitedir/pygtk*
%py_platsitedir/gi
%py_platsitedir/glib
%py_platsitedir/gobject
%py_platsitedir/gtk-2.0/

%files -n %libname
%defattr(-,root,root)
%_libdir/libpyglib-%api-python.so.%{major}*

%files devel
%defattr(-,root,root)
%_bindir/pygobject-codegen-2.0
%_libdir/pkgconfig/*.pc
%_libdir/libpyglib-%api-python.so
%_libdir/libpyglib-%api-python.la
%_includedir/pygtk-2.0/
%_datadir/gtk-doc/html/pygobject/
%_datadir/pygobject/
