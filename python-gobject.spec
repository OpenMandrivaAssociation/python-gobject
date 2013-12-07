%define oname pygobject

%define api 2.0
%define major 0
%define libname %mklibname pyglib %{api} %{major}

Summary:	GObject Python bindings 
Name:		python-gobject
Version:	2.28.6
Release:	5
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pygobject/%{oname}-%{version}.tar.xz
Patch0:		pygobject-2.16.1-fixdetection.patch
Patch1:		pygobject-2.28.2-fix-link.patch

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	pkgconfig(python)

Provides:	python-gobject2 = %{version}-%{release}

%description
This archive contains bindings for the GObject, to be used in Python
It is a fairly complete set of bindings, it's already rather useful, 
and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).

%package -n %{libname}
Group:		System/Libraries
Summary:	Python Glib bindings shared library

%description -n %{libname}
This archive contains bindings for the GObject, to be used in Python
It is a fairly complete set of bindings, it's already rather useful, 
and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).

%package devel
Group:		Development/C
Summary:	Python-gobject development files
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description devel
This contains the python-gobject development files, including C
header, pkg-config file, gtk-doc generated API documentation and a code
generation tool.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-introspection

%make LIBS='-lpython2.7'

%install
%makeinstall_std
#gw this must be executable, it is used for building docs, e.g. in pyclutter
chmod 755 %{buildroot}%{_datadir}/pygobject/xsl/fixxref.py

%files
%{py_platsitedir}/pygtk*
%{py_platsitedir}/glib
%{py_platsitedir}/gobject
%{py_platsitedir}/gtk-2.0/

%files -n %{libname}
%{_libdir}/libpyglib-%{api}-python.so.%{major}*

%files devel
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/pygobject-codegen-2.0
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpyglib-%{api}-python.so
%{_includedir}/pygtk-2.0/
%{_datadir}/gtk-doc/html/pygobject/
%{_datadir}/pygobject/

