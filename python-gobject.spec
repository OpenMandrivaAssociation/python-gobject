%define oname pygobject

%define api 2.0
%define major 0
%define libname %mklibname pyglib %{api} %{major}

Summary:	GObject Python bindings 
Name:		python-gobject
Version:	2.28.6
Release:	4
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
rm -rf %{buildroot}
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



%changelog
* Fri Mar 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.28.6-3
+ Revision: 785416
- rebuild
- cleaned up spec

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.28.6-2
+ Revision: 722025
- Rebuild with newer libpng.

* Mon Jun 13 2011 Götz Waschk <waschk@mandriva.org> 2.28.6-1
+ Revision: 684931
- new version
- xz tarball

* Tue Apr 19 2011 Götz Waschk <waschk@mandriva.org> 2.28.4-1
+ Revision: 655907
- update to new version 2.28.4

* Thu Mar 24 2011 Funda Wang <fwang@mandriva.org> 2.28.3-2
+ Revision: 648271
- more linakge fix

  + Götz Waschk <waschk@mandriva.org>
    - new version
    - bump deps
    - drop patch 2
    - update file list

* Mon Mar 21 2011 Funda Wang <fwang@mandriva.org> 2.26.0-3
+ Revision: 647380
- rebuild

* Sat Oct 30 2010 Olivier Thauvin <nanardon@mandriva.org> 2.26.0-2mdv2011.0
+ Revision: 590343
- rebuild for python

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2011.0
+ Revision: 581442
- new version
- update patch 2

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.21.5-1mdv2011.0
+ Revision: 563398
- new version
- build with gobject-introspection

* Mon May 31 2010 Funda Wang <fwang@mandriva.org> 2.21.1-2mdv2010.1
+ Revision: 546766
- fix shared library linkage (mdv#59571)

* Sat Jan 02 2010 Götz Waschk <waschk@mandriva.org> 2.21.1-1mdv2010.1
+ Revision: 485574
- update to new version 2.21.1

* Fri Dec 18 2009 Götz Waschk <waschk@mandriva.org> 2.21.0-1mdv2010.1
+ Revision: 479908
- new version
- bump deps
- update file list

* Wed Sep 23 2009 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2010.0
+ Revision: 448019
- update to new version 2.20.0

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2010.0
+ Revision: 415194
- new version
- update file list

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 2.18.0-2mdv2010.0
+ Revision: 410191
- make fixxref executable
- move codegen files to devel package

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2010.0
+ Revision: 379436
- new version
- drop patch 1
- update file list

* Wed May 13 2009 Götz Waschk <waschk@mandriva.org> 2.17.0-3mdv2010.0
+ Revision: 375244
- fix devel deps

* Wed May 13 2009 Götz Waschk <waschk@mandriva.org> 2.17.0-2mdv2010.0
+ Revision: 375229
- make ffi dep private

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.17.0-1mdv2010.0
+ Revision: 374166
- new version
- drop patch 1

* Mon Feb 23 2009 Götz Waschk <waschk@mandriva.org> 2.16.1-2mdv2009.1
+ Revision: 344032
- fix patch 0 (bug #48122)

* Sun Feb 22 2009 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2009.1
+ Revision: 343818
- new version
- rediff patch 0

* Sun Jan 04 2009 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2009.1
+ Revision: 324715
- update to new version 2.16.0

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 2.15.4-2mdv2009.1
+ Revision: 318414
- fix format error
- rebuild for new python

* Wed Sep 03 2008 Götz Waschk <waschk@mandriva.org> 2.15.4-1mdv2009.0
+ Revision: 279585
- new version

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 2.15.3-3mdv2009.0
+ Revision: 278402
- fix dep on libffi (b.g.o bug #550231)

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 2.15.3-2mdv2009.0
+ Revision: 278211
- build with libffi

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 2.15.3-1mdv2009.0
+ Revision: 278072
- new version
- drop patch 1

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 2.15.2-2mdv2009.0
+ Revision: 262917
- fix for bug 42467 (pygtk apps don't launch)

* Sun Jul 27 2008 Götz Waschk <waschk@mandriva.org> 2.15.2-1mdv2009.0
+ Revision: 250612
- new version
- add package for libpyglib
- disable --no-undefined

* Wed Jul 16 2008 Götz Waschk <waschk@mandriva.org> 2.15.1-1mdv2009.0
+ Revision: 236290
- new version
- update file list
- remove conflict with pygtk

* Tue Jul 15 2008 Götz Waschk <waschk@mandriva.org> 2.15.0-1mdv2009.0
+ Revision: 235854
- update license
- new version
- update file list
- add conflict with old pygtk2.0-devel
- update description

* Mon May 26 2008 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2009.0
+ Revision: 211295
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-not-capitalized

* Thu Jan 03 2008 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdv2008.1
+ Revision: 142105
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 20 2007 Olivier Blin <blino@mandriva.org> 2.14.0-2mdv2008.0
+ Revision: 91462
- move development doc in devel package

* Sun Sep 16 2007 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdv2008.0
+ Revision: 88449
- new version

* Sat Jul 07 2007 Götz Waschk <waschk@mandriva.org> 2.13.2-1mdv2008.0
+ Revision: 49435
- new version

* Thu Jun 28 2007 Helio Chissini de Castro <helio@mandriva.com> 2.13.1-3mdv2008.0
+ Revision: 45502
- MOve devel files for devel place

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 2.13.1-2mdv2008.0
+ Revision: 36193
- rebuild with correct optflags

  + Götz Waschk <waschk@mandriva.org>
    - new version


* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 2.12.3-2mdv2007.0
+ Revision: 87908
- rebuild

* Wed Nov 22 2006 Götz Waschk <waschk@mandriva.org> 2.12.3-1mdv2007.1
+ Revision: 86166
- new version
- unpack patch
- Import python-gobject

* Thu Oct 05 2006 Götz Waschk <waschk@mandriva.org> 2.12.2-1mdv2007.0
- New version 2.12.2

* Wed Sep 06 2006 Götz Waschk <waschk@mandriva.org> 2.12.1-1mdv2007.0
- New release 2.12.1

* Tue Aug 29 2006 Götz Waschk <waschk@mandriva.org> 2.11.4-1mdv2007.0
- New release 2.11.4

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.11.3-1mdv2007.0
- New release 2.11.3

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.11.2-1mdv2007.0
- New release 2.11.2

* Sun Aug 06 2006 Götz Waschk <waschk@mandriva.org> 2.11.1-1mdv2007.0
- update file list
- disable parallel make
- New release 2.11.1

* Fri Jul 14 2006 Götz Waschk <waschk@mandriva.org> 2.11.0-1mdv2007.0
- update the patch
- New release 2.11.0

* Wed Apr 12 2006 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdk
- update patch
- New release 2.10.1

* Mon Mar 13 2006 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdk
- New release 2.10.0

* Thu Feb 23 2006 Frederic Crozat <fcrozat@mandriva.com> 2.9.1-2mdk
- Allow compilation with old distro

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 2.9.1-1mdk
- New release 2.9.1

* Wed Jan 11 2006 Michael Scherer <misc@mandriva.org> 2.9.0-3mdk
- Use new python macro

* Tue Jan 10 2006 Götz Waschk <waschk@mandriva.org> 2.9.0-2mdk
- add conflict to ease upgrade

* Tue Jan 10 2006 Götz Waschk <waschk@mandriva.org> 2.9.0-1mdk
- initial package

