%define oname pygobject

%define api 3.0
%define major 0

#define _disable_rebuild_configure 1
#define _disable_lto 1

Summary:	GObject Python bindings 
Name:		python-gobject
Version:	3.28.2
Release:	2
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pygobject/%(echo %{version} |cut -d. -f1-2)/%{oname}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(py3cairo)
BuildRequires:	pkgconfig(python3)

%description
This archive contains bindings for the GObject, to be used in Python
It is a fairly complete set of bindings, it's already rather useful, 
and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).

%package -n python2-gobject
Summary:	Python 2.x GObject bindings
Group:		Development/Python

%description -n python2-gobject
This archive contains bindings for the GObject, to be used in Python2
It is a fairly complete set of bindings, it's already rather useful, 
and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).

%package devel
Group:		Development/C
Summary:	Python-gobject development files
Requires:	%{name} = %{version}-%{release}

%description devel
This contains the python-gobject development files, including C
header, pkg-config file, gtk-doc generated API documentation and a code
generation tool.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

export CC=%{__cc}
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"

mkdir py2
cd py2
export PYTHON=%__python2
../configure \
	--prefix=%{_prefix} --libdir=%{_libdir} \
	--enable-cairo
cd ..

mkdir py3
cd py3
export PYTHON=%__python
../configure \
	--prefix=%{_prefix} --libdir=%{_libdir} \
	--enable-cairo

%build
cd py2
%make_build LIBS='-lpython2.7'
cd ../py3
%make_build LIBS='-lpython3.7m'

%install
cd py2
%make_install
cd ../py3
%make_install


%files
%{py_platsitedir}/pygobject-*.egg-info
%{py_platsitedir}/pygtkcompat
%{py_platsitedir}/gi

%files -n python2-gobject
%{py2_platsitedir}/pygobject-*.egg-info
%{py2_platsitedir}/pygtkcompat
%{py2_platsitedir}/gi

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/pygobject-%{api}
